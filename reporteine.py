from io import TextIOWrapper
import os
import shutil
import pathlib
import subprocess
import WS_orga_INE
from xlsxchef import xlsxChef
from datetime import datetime
from funcionesINE import FuncionesINE
from funcionesjo import mes_by_ordinal

"""
data := {
    'nombre':str,
    'mes':int,
    'anio':int,
    'presentacion': str,
    'plantillas': list[files]
    'capitulos':[
        {
            'titulo': str,
            'resumen': str,
            'anexo': bool,
            'sub_capitulos':[
                {
                    'titulo': str,
                    'titulo_grafico': str,
                    'descripcion_grafico': str,
                    'descripcion': str,
                    'fuente': str,
                    'tipo_grafico': str,
                    'data': list[tuple[str, int]],
                    'opciones_grafica':dict
                }
            ]
        }
    ]
}
"""
class ReporteINE:
    """
    Clase para la creacion de reportes estilo INE.

    Attributes
    ----------
    nombre : str
        nombre del reporte, sera el titulo principal del documento.
    fecha_inicio : str
        
    fecha_final : str
        

    Methods
    -------
    hacer_graficas()
        
    """
    def __init__(self,nombre: str, anio: int, mes: int) -> None:
        self.__data = {}
        self.__data['nombre'] = nombre
        self.__data['capitulos'] = []
        self._indice = -1
        self.anio = anio
        self.mes = mes
        # hacer directorio para guardar documentos
        marca_temporal = datetime.strftime(datetime.today(), "%d-%m-%Y_%H_%M_%S")
        parent_dir = pathlib.Path().resolve()
        self.__path = os.path.join(parent_dir, marca_temporal)
        # arbol de carpetas
        os.mkdir(self.__path)
        DIRECTORIOS = (
            "libros",
            "csv",
            "csv_cocinado",
            "graficas",
            "descripciones",
            "plantilla",
            "tex"
        )
        for dir in DIRECTORIOS:
            os.mkdir(os.path.join(self.__path, dir))
        # copiar archivos plantilla
        FUENTES = (
            "OpenSans-CondLight.ttf",
            "OpenSans-CondBold.ttf",
            "OpenSans-CondLightItalic.ttf")
        for fuente in FUENTES:
            shutil.copyfile(
                f"Fuentes/{fuente}",
                os.path.join(self.__path, f"plantilla/{fuente}"))
        ARCHIVOS = (
            "Carta3.tex",
            "contraportada.pdf",
            "fondo-capitulo.pdf",
            "fondo-capitulo-no-descripcion.pdf",
            "parte.pdf",
            "portada.pdf",
            "topeven3.pdf",
            "topodd3.pdf")
        for archivo in ARCHIVOS:
            shutil.copyfile(
                f"Plantilla/{archivo}",
                os.path.join(self.__path, f"plantilla/{archivo}"))
        TEXS = (
            "participantes.tex",
            "glosario.tex",
            "formulas.tex",
            "dgrm_ipc_01.tex",
            "dgrm_ipc_02.tex",
            "dgrm_ipc_03.tex",
            "dgrm_ipc_04.tex"
        )
        for tex in TEXS:
            shutil.copyfile(
                f"Plantilla/{tex}",
                os.path.join(self.__path, f"tex/{tex}"))
        # cargar modulo de R 
        self.f_INE = FuncionesINE()
        # hacer junta directiva
        if WS_orga_INE.conexionQ():
            try:
                WS_orga_INE.junta_directiva(ruta=os.path.join(self.__path, "tex"))
            except:
                shutil.copyfile(
                    "Plantilla/organizacion.tex",
                    os.path.join(self.__path, "tex/organizacion.tex")) 
        else:
            shutil.copyfile(
                "Plantilla/organizacion.tex",
                os.path.join(self.__path, "tex/organizacion.tex")) 

    def presentacion(self, texto):
        ruta = os.path.join(self.__path, f"tex/presentacion.tex")
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(texto)

    def aproximador(self, datos, precision: int = 2):
        datos_aprox = []
        for dato in datos:
            x = dato[0]
            y = round(dato[1], precision)
            datos_aprox.append((x, y))
        return datos_aprox

    def agregar_capitulo(self, titulo: str, resumen: str = "", anexo: bool = False) -> None:
        capitulo_nuevo = {
            "titulo": titulo,
            "resumen": resumen,
            "anexo": anexo,
            "sub_capitulos": []
        }
        self.__data.get("capitulos").append(capitulo_nuevo)
        self._indice += 1

    def agregar_subcapitulo(
        self,
        titulo: str,
        titulo_grafico: str,
        descripcion_grafico: str,
        descripcion: str,
        fuente: str,
        tipo_grafico: str,
        data: tuple,
        opciones_grafico: dict
        ) -> None:
        sub_cap = {}
        sub_cap["titulo"] = titulo
        sub_cap["titulo_grafico"] = titulo_grafico
        sub_cap["descripcion_grafico"] = descripcion_grafico
        sub_cap["descripcion"] = descripcion
        sub_cap["fuente"] = fuente
        sub_cap["tipo_grafico"] = tipo_grafico
        sub_cap["opciones_grafico"] = opciones_grafico
        sub_cap["data"] = data
        self.__data.get('capitulos')[self._indice]['sub_capitulos'].append(sub_cap)
    
    def escribir_libros(self) -> None:
        for i, capitulo in enumerate(self.__data['capitulos']):
            i += 1
            nombre_doc = capitulo["titulo"]
            csv_chef = xlsxChef(
                tipo="csv",
                path=self.__path,
                nombre=nombre_doc,
                NoCapitulo=i
            )
            cocinado_chef = xlsxChef(
                tipo="cocinado",
                path=self.__path,
                nombre=nombre_doc,
                NoCapitulo=i
            )
            sub_capitulos = capitulo["sub_capitulos"]
            for sub_capitulo in sub_capitulos:
                tipo_grafico = sub_capitulo["tipo_grafico"]
                if tipo_grafico in ("lineal", "barra", "columna"):
                    encabezados = True 
                    if len(sub_capitulo["data"][0]) > 2:
                        encabezados = False
                    k = sub_capitulos.index(sub_capitulo) + 1
                    try:
                        prec = sub_capitulo["opciones_grafico"]["precision"]
                    except KeyError:
                        prec = 2
                    csv_chef.escribir_hoja(
                        # realizar aproximacion de datos
                        datos=self.aproximador(sub_capitulo["data"], prec),
                        ordinal=k,
                        encabezadosXY=encabezados
                    )
                    datos_cocinado = (
                        sub_capitulo["titulo"],
                        sub_capitulo["titulo_grafico"],
                        sub_capitulo["descripcion_grafico"],
                        sub_capitulo["descripcion"]
                    )
                    cocinado_chef.escribir_hoja(
                        datos=datos_cocinado,
                        ordinal=k
                    )
            cocinado_chef.cerrar_libro()
            csv_chef.cerrar_libro()
    
    def generar_csv(self):
        ruta = self.__path.replace("\\", "/")
        i = 0
        for capitulo in self.__data['capitulos']:
            i += 1
            nombre = capitulo['titulo'].title().replace(" ", "")
            libro_cocinado = f"{nombre}_cocinado.xlsx"
            libro_csv = f"{nombre}_csv.xlsx"
            csv_path = os.path.join(self.__path, "csv")
            os.mkdir(os.path.join(csv_path, str(i)))
            self.f_INE.escribirCSVcocinado(
                ruta_libro=f'{ruta}/libros/{libro_cocinado}',
                ruta_salida=f"{ruta}/csv_cocinado"
            )
            self.f_INE.escribirCSV(
                ruta_libro=f'{ruta}/libros/{libro_csv}',
                ruta_salida=f"{ruta}/csv/{i}")
    
    def hacer_graficas(self):
        ruta_tex = self.__path.replace("\\", "/") + "/graficas"
        for i, capitulo in enumerate(self.__data['capitulos']):
            csv_path = os.path.join(self.__path, f"csv\\{i + 1}").replace("\\", "/")
            self.f_INE.cargaMasiva(csv_path)
            sub_capitulos = capitulo["sub_capitulos"]
            for indice, sub_capitulo in enumerate(sub_capitulos):
                indice_natural = str(indice + 1).rjust(2, "0")
                referencia = f"{i + 1}_{indice_natural}"
                tipo_grafico = sub_capitulo["tipo_grafico"]
                if tipo_grafico == "lineal":
                    self.f_INE.graficaLinea(
                        data_index=referencia,
                        ruta_salida=ruta_tex,
                        nombre=referencia,
                        **sub_capitulo["opciones_grafico"]
                    )
                elif tipo_grafico == "barra":
                    self.f_INE.graficaBar(
                        data_index=referencia,
                        ruta_salida=ruta_tex,
                        nombre=referencia,
                        **sub_capitulo["opciones_grafico"]
                    )
                elif tipo_grafico == "columna":
                    self.f_INE.graficaCol(
                        data_index=referencia,
                        ruta_salida=ruta_tex,
                        nombre=referencia,
                        **sub_capitulo["opciones_grafico"]
                    )
                elif tipo_grafico == "tabla":
                    t_inflacion = False
                    if "Inflación" in sub_capitulo["titulo"]:
                         t_inflacion = True
                    self.tabla_LaTeX(
                        datos=sub_capitulo["data"],
                        ruta_salida=os.path.join(self.__path, "graficas"),
                        nombre=referencia,
                        tabla_inflacion=t_inflacion,
                        **sub_capitulo["opciones_grafico"])
    
    def hacer_descripciones(self) -> None:
        i = 0
        for capitulo in self.__data['capitulos']:
            i += 1
            j = 0
            sub_capitulos = capitulo["sub_capitulos"]
            for sub_capitulo in sub_capitulos:
                j += 1
                j_str = str(j).rjust(2, "0")
                path = os.path.join(self.__path, f"descripciones\\{i}_{j_str}")
                os.mkdir(path)
                informacion = (
                    "descripcion",
                    "titulo",
                    "titulo_grafico",
                    "descripcion",
                    "descripcion_grafico",
                    "fuente")
                for dato in informacion:
                    with open(os.path.join(path, dato + ".tex"), "w", encoding="utf-8") as f:
                        f.write(self.formato_LaTeX(sub_capitulo[dato]))
                        f.close()
    
    def hacer_capitulos(self):
        i = 0
        for capitulo in self.__data['capitulos']:
            i += 1
            j = 0
            file_name = capitulo["titulo"].replace(" ", "_")
            path = os.path.join(self.__path, f"tex/{file_name}.tex")
            sub_capitulos = capitulo["sub_capitulos"]
            with open(path, "w", encoding='utf-8') as f:
                for sub_capitulo in sub_capitulos:
                    j += 1
                    j_str = str(j).rjust(2, "0")
                    carpeta = f"descripciones/{i}_{j_str}"
                    titulo =  sub_capitulo["titulo"]
                    f.write("\\cajita{%\n" + titulo + "}%\n")
                    f.write("{%\n\\input{" + carpeta + "/descripcion.tex" + "}}%\n")
                    f.write("{%\n\\input{" + carpeta + "/titulo_grafico.tex" + "}}%\n")
                    f.write("{%\n\\input{" + carpeta + "/descripcion_grafico.tex" + "}}%\n")
                    if sub_capitulo["tipo_grafico"] in ("lineal", "barra", "columna"):
                        f.write("{%\n\\begin{tikzpicture}[x=1pt,y=1pt]\\input{" + f"graficas/{i}_{j_str}.tex" + "}\\end{tikzpicture}}%\n")
                    elif sub_capitulo["tipo_grafico"] in ("mapa"):
                        f.write("{%\n\\includegraphics[width=52\\cuadri]{" + f"graficas/{i}_{j_str}.pdf" + "}%\n")
                    elif sub_capitulo["tipo_grafico"] in ("tabla"):
                        f.write("{%\n\\input{" + f"graficas/{i}_{j_str}.tex" + "}}%\n")
                    f.write("{%\n\\input{" + carpeta + "/fuente.tex" + "}}%\n\n")
                f.close()

    def escribir_capitulo(self, capitulo, f: TextIOWrapper):
        titulo = capitulo["titulo"]
        file_name = titulo.replace(" ", "_") + ".tex"
        resumen = self.formato_LaTeX(capitulo["resumen"])
        f.write("\\INEchaptercarta{" + titulo + "}{" + resumen + "}\n")
        f.write("\\input{tex/" + file_name + "}\n")

    def hacer_portada(self):
        path = os.path.join(self.__path, f"tex/portada.tex")
        mes_1 = mes_by_ordinal(self.mes, abreviado=False)
        anio_1 = self.anio
        if self.mes == 1:
            anio_2 = anio_1 - 1
            mes_2 = mes_by_ordinal(12, abreviado=False)
        else:
            mes_2 = mes_by_ordinal(self.mes - 1, abreviado=False)
            anio_2 = anio_1
        with open(path, 'w', encoding='utf-8') as f:
            f.write("\\includepdf[pagecommand={\n")
            f.write("\\begin{tikzpicture}[remember picture, overlay]\n")
            f.write("\\node[nome] at ([yshift=4cm] current page) {\\color{white}{\\mgrande República de Guatemala:}};\n")
            f.write("\\node[nome] at ([yshift=2.3cm] current page) {\\color{white}{\\mgrande Índice de Precios al Consumidor}};\n")
            f.write("\\node[nome] at ([yshift=0.6cm] current page) {\\color{white}{\\mgrande "+ f"{mes_1} {anio_1}" + "}};\n")
            f.write("\\node at ([yshift=-12cm] current page) {\\color{white}{\\LARGE Guatemala, " + f"{mes_2.lower()} de {anio_2}" + "}};\n")
            f.write("\\end{tikzpicture}}\n")
            f.write("]{plantilla/portada.pdf}\n")

    def hacer_cuerpo(self):
        nombre = self.__data["nombre"].replace(" ", "_")
        path = os.path.join(self.__path, f"{nombre}.tex")
        with open(path, "w", encoding='utf-8') as f:
            f.write("\\input{plantilla/Carta3.tex}\n")
            f.write("\\renewcommand{\\partes}{No por favor}\n")
            f.write("\\renewcommand{\\titulodoc}{" + self.formato_LaTeX(self.__data["nombre"]) + "}\n")
            f.write("\\newcommand{\\ra}[1]{\\renewcommand{\\arraystretch}{#1}}\n")
            f.write("\\usepackage{xcolor}\n")
            f.write("\\newcommand{\\mgrande}{\\fontsize{40}{48} \\selectfont}\n")
            f.write("\\tikzstyle{nome}=[anchor=center, minimum height=2cm, minimum width=9cm, text width=15cm]\n")
            f.write("\\begin{document}\n")
            f.write("\\pagestyle{empty}\n")
            f.write("\\input{tex/portada.tex}\n")
            f.write("\\newpage\n")
            # preambulo
            f.write("\\pagestyle{soloarriba}\n")
            f.write("\\clearpage\n")
            f.write("$\\ $\n")
            f.write("\\vfill\n")
            f.write("\\noindent\\begin{tabular}{p{0.9cm}p{6.8cm}}\n")
            hoy = datetime.strftime(datetime.today(), "%Y")
            f.write(f"& {hoy}.$\,$ Guatemala, Centro América\\\\\n")
            f.write("&\\Bold Instituto Nacional de Estadística\\\\[-0.4cm]\n")
            f.write("&\\color{blue!50!black}\\url{www.ine.gob.gt}\\\\[0.9cm]\n")
            f.write("\\end{tabular}\\\\\n")
            f.write("\\noindent\\begin{tabular}{p{0.9cm}p{6.8cm}}\n")
            f.write("& Está permitida la reproducción parcial o total de los contenidos de este documento con la mención de la fuente. \\\\[0.5cm]\n")
            f.write("& Este documento fue elaborado empleando Python, {\\Sans R}, QGIS y {\\Logos \\XeLaTeX}.\\\\\n")
            f.write("\\end{tabular}\n")
            f.write("\\clearpage\n")
            f.write("\\clearpage\n")
            f.write("\\newpage $\\ $\n")
            f.write("$\\ $\n")
            f.write("\\vspace{0.0cm}\n")
            f.write("\\begin{center}\n")
            f.write("\\input{tex/organizacion.tex}\n") # organigrama del INE
            f.write("\\end{center}\n")
            f.write("\\clearpage\n")
            f.write("$\\ $\n")
            f.write("\\vspace{0.0cm}\n")
            f.write("\\begin{center}\n")
            f.write("\\input{tex/participantes.tex}\n") # participantes
            f.write("\\end{center}\n")
            f.write("\\vfill\n")
            f.write("\\hrule\n")
            f.write("\\cleardoublepage\n")
            f.write("$\\ $\\\\[2cm]\n")
            f.write("\\noindent {\\Bold \\huge Presentación}\n")
            f.write("\\\\\\\\\n")
            f.write("\\input{tex/presentacion.tex}\n")
            f.write("\\cleardoublepage\n")
            # fin-preambulo
            f.write("\\tableofcontents\n")
            f.write("\\pagestyle{estandar}\n")
            f.write("\\setcounter{page}{0}\n")
            for capitulo in self.__data["capitulos"]:
                if not capitulo['anexo']:
                    self.escribir_capitulo(capitulo, f)
            # hacer apendice
            f.write("\\appendix\n")
            f.write("\\INEchaptercarta{Glosario}{}\n")
            f.write("\\input{tex/glosario.tex}\n")
            f.write("\\INEchaptercarta{Principales fórmulas de cálculo}{}\n")
            f.write("\\input{tex/formulas.tex}\n")
            f.write("\\includepdf{plantilla/contraportada.pdf}\n")
            for capitulo in self.__data["capitulos"]:
                if capitulo['anexo']:
                    self.escribir_capitulo(capitulo, f)
            f.write("\\end{document}\n")
            f.close()
            
    def compilar_reporte(self):
        nombre = self.__data["nombre"].replace(" ", "_")
        path = os.path.join(self.__path, f"{nombre}.tex")
        subprocess.call(["xelatex", "-synctex=1", "-interaction=nonstopmode", path])

    def crear_reporte(self):
        self.escribir_libros()
        self.generar_csv()
        self.hacer_graficas()
        self.hacer_descripciones()
        self.hacer_capitulos()
        self.hacer_portada()
        self.hacer_cuerpo()

    def formato_LaTeX(self, cadena: str) -> str:
        CARACTERES_ESPECIALES = ('#', '$', '%', '&', '~', '_', '^')
        for caracter in CARACTERES_ESPECIALES:
           cadena = cadena.replace(caracter, "{\\" + caracter + "}")
        return cadena

    def tabla_LaTeX(
        self,
        datos,
        ruta_salida,
        nombre,
        precision: int = 2,
        tabla_inflacion: bool = False):
        with open(os.path.join(ruta_salida, f"{nombre}.tex"), "w", encoding="utf-8") as f:
            f.write("\\setlength{\\arrayrulewidth}{1.5pt}\n")
            f.write("\\definecolor{Fcolor}{HTML}{e5e5fa}\n")
            f.write("\\definecolor{Lcolor}{HTML}{4d80ff}\n")
            # si es tabla de inflacion lleva esa cosa sobre los meses de "Inflacion interanual a"
            if tabla_inflacion:
                f.write("\\setlength{\\aboverulesep}{-1pt}\n")
                f.write("\\setlength{\\belowrulesep}{0pt}\n")
            alinacion = len(datos[0])*"c"
            f.write("\\begin{tabular}{" + alinacion + "}\n")
            f.write("\\arrayrulecolor{Lcolor} \hline\n")
            # si es tabla de inflacion lleva esa cosa sobre los meses de "Inflacion interanual a"
            if tabla_inflacion:
                f.write("\\rowcolor{Fcolor} & \\multicolumn{2}{c}{\\textbf{Inflacion interanual a}}\\\\\n")
                f.write("\\cmidrule[0.9pt]{2-3}\n")
            f.write("\\rowcolor{Fcolor} ")
            i = 0
            for encabezado in datos[0]:
                i += 1
                f.write("\\textbf{" + encabezado + "}")
                if i != len(datos[0]):
                    f.write(" & ")
                else:
                    f.write("\\\\\n")
            f.write("\\hline\n")
            f.write("\\rowcolor{white} ")
            for i in range(1, len(datos)):
                j = 0
                for celda in datos[i]:
                    j += 1
                    if type(celda) is str:
                        f.write(f"{celda}")
                    else:
                        if precision == 1:
                            f.write(f"{float(celda):.1f}")
                        elif precision == 2:
                            f.write(f"{float(celda):.2f}")
                        elif precision == 3:
                            f.write(f"{float(celda):.3f}")
                        elif precision == 4:
                            f.write(f"{float(celda):.4f}")
                        else:
                            f.write(f"{float(celda):.4f}")
                    if j != len(datos[i]):
                        f.write(" & ")
                    else:
                        f.write("\\\\\n")
            f.write("\\hline\n")
            f.write("\\end{tabular}\n")
            f.close()