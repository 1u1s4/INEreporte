import os
import pathlib
import shutil
import subprocess
import pkg_resources
import pandas as pd
from datetime import datetime
from io import TextIOWrapper

from .WS_orga_INE import conexionQ, junta_directiva
from .funcionesINE import FuncionesINE
from .utils import quitar_tildes, formato_LaTeX, nombre_carpeta
from funcionesjo import mes_by_ordinal
from colorimapgt import mapa

class ReporteINE:
    def __init__(
        self,
        nombre_reporte: str,
        anio: int,
        mes: int,
        periodo: str,
        direccion: str = 'DIEC',
        r_home: str = None) -> None:
        self.__data = {}
        self.__data['nombre'] = nombre_reporte
        self.__data['capitulos'] = []
        self._indice = -1
        self.nombre_reporte = nombre_reporte
        self.periodo = periodo
        self.anio = anio
        self.mes = mes
        self.direccion = direccion
        # hacer directorio para guardar documentos
        parent_dir = pathlib.Path().resolve()
        self.__path = os.path.join(parent_dir, nombre_carpeta(nombre_reporte))
        # arbol de carpetas
        os.mkdir(self.__path)
        DIRECTORIOS = (
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
            "OpenSans-CondLightItalic.ttf"
        )
        for fuente in FUENTES:
            fuente_path = pkg_resources.resource_filename(__name__, f"Fuentes/{fuente}")
            shutil.copyfile(
                fuente_path,
                os.path.join(self.__path, f"plantilla/{fuente}"))
        # copiar carta3.tex
        shutil.copyfile(
            pkg_resources.resource_filename(__name__, f"Plantilla/Carta3.tex"),
            os.path.join(self.__path, f"plantilla/Carta3.tex")
        )
        ARCHIVOS = (
            "contraportada.pdf",
            "fondo-capitulo.pdf",
            "fondo-capitulo-no-descripcion.pdf",
            "parte.pdf",
            "portada.pdf",
            "topeven3.pdf",
            "topodd3.pdf"
        )
        for archivo in ARCHIVOS:
            archivo_path = pkg_resources.resource_filename(__name__, f"Direcciones/{direccion}/{archivo}")
            shutil.copyfile(
                archivo_path,
                os.path.join(self.__path, f"plantilla/{archivo}"))
        TEXS = (
            "participantes.tex",
            "glosario.tex"
        )
        for tex in TEXS:
            tex_path = pkg_resources.resource_filename(__name__, f"Plantilla/{tex}")
            shutil.copyfile(
                tex_path,
                os.path.join(self.__path, f"tex/{tex}"))
        # banderas para saber si se ha creado el archivo
        self.__formulas = False
        # cargar modulo de R 
        self.f_INE = FuncionesINE(r_home)
        # hacer junta directiva
        organizacion_tex_path = pkg_resources.resource_filename(__name__, "Plantilla/organizacion.tex")
        if conexionQ():
            try:
                junta_directiva(ruta=os.path.join(self.__path, "tex"))
            except:
                shutil.copyfile(
                    organizacion_tex_path,
                    os.path.join(self.__path, "tex/organizacion.tex")) 
        else:
            shutil.copyfile(
                organizacion_tex_path,
                os.path.join(self.__path, "tex/organizacion.tex"))

    def set_formulas(self, ruta: str) -> None:
        """Copia archivo de formulas a la carpeta del reporte"""
        shutil.copyfile(
            ruta,
            os.path.join(self.__path, f"tex/formulas.tex"))
        self.__formulas = True
    
    def set_portada(self, ruta: str) -> None:
        """Copia archivo de portada a la carpeta del reporte"""
        shutil.copyfile(
            ruta,
            os.path.join(self.__path, f"plantilla/portada.pdf"))

    def get_data(self) -> dict:
        return self.__data

    def presentacion(self, texto):
        ruta = os.path.join(self.__path, f"tex/presentacion.tex")
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(texto)

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
            data: tuple | str,
            opciones_grafico: dict
            ) -> None:
        sub_cap = {
            "titulo": titulo,
            "titulo_grafico": titulo_grafico,
            "descripcion_grafico": descripcion_grafico,
            "descripcion": descripcion,
            "fuente": fuente,
            "tipo_grafico": tipo_grafico,
            "opciones_grafico": opciones_grafico,
            "data": data
        }
        self.__data.get('capitulos')[self._indice]['sub_capitulos'].append(sub_cap)
            
    def hacer_graficas(self):
        ruta_salida = self.__path.replace("\\", "/") + "/graficas"
        for i, capitulo in enumerate(self.__data['capitulos']):

            sub_capitulos = capitulo["sub_capitulos"]
            for indice, sub_capitulo in enumerate(sub_capitulos):
                indice_natural = str(indice + 1).rjust(2, "0")
                referencia = f"{i + 1}_{indice_natural}"
                tipo_grafico = sub_capitulo["tipo_grafico"]
                if tipo_grafico == "lineal":
                    self.f_INE.graficaLinea(
                        data=pd.DataFrame(sub_capitulo['data'], columns=['x', 'y']),
                        ruta_salida=ruta_salida,
                        nombre=referencia,
                        **sub_capitulo["opciones_grafico"]
                    )
                elif tipo_grafico == "barra":
                    self.f_INE.graficaBar(
                        data=pd.DataFrame(sub_capitulo['data'], columns=['x', 'y']),
                        ruta_salida=ruta_salida,
                        nombre=referencia,
                        **sub_capitulo["opciones_grafico"]
                    )
                elif tipo_grafico == "columna":
                    self.f_INE.graficaCol(
                        data=pd.DataFrame(sub_capitulo['data'], columns=['x', 'y']),
                        ruta_salida=ruta_salida,
                        nombre=referencia,
                        **sub_capitulo["opciones_grafico"]
                    )
                elif tipo_grafico == "tabla":
                    t_inflacion = False
                    if "Inflación" in sub_capitulo["titulo"]:
                         t_inflacion = True
                    self.f_INE.tabla_LaTeX(
                        datos=sub_capitulo["data"],
                        ruta_salida=os.path.join(self.__path, "graficas"),
                        nombre=referencia,
                        tabla_inflacion=t_inflacion,
                        **sub_capitulo["opciones_grafico"]
                    )
                elif tipo_grafico == "diagrama_tikz":
                    ruta_diagrama = sub_capitulo["data"]
                    nombre_destino = f"{referencia}.tex"
                    shutil.copyfile(
                        ruta_diagrama,
                        os.path.join(self.__path, "graficas", nombre_destino)
                    )
                elif tipo_grafico == "mapa_colorimetrico":
                    """
                    data tiene que ser un dataframe con las columnas:
                    - region: 'Región I', 'Región II', 'Región III', 'Región IV', 'Región V', 'Región VI', 'Región VII', 'Región VIII'
                    - valores: los valores correspondientes a cada región
                    """
                    data_pandas = pd.DataFrame(sub_capitulo["data"], columns=["region", "valor"])
                    mapa_color = mapa.Mapa(
                        data=data_pandas,
                        nombre_archivo=f"{referencia}.tex",
                        output_dir=ruta_salida,
                        **sub_capitulo["opciones_grafico"]
                    )
                    mapa_color.hacer_mapa()
                    mapa_color.compilar()
                    mapa_color.limpiar()
                """
                elif tipo_grafico == "tabla_larga":
                    self.export_to_longtable(
                        df=sub_capitulo["data"],
                        filename=referencia,
                        ruta_salida=ruta_tex
                    )
                """
    
    def hacer_descripciones(self) -> None:
        for i, capitulo in enumerate(self.__data['capitulos']):
            i += 1
            sub_capitulos = capitulo["sub_capitulos"]
            for j, sub_capitulo in enumerate(sub_capitulos):
                j += 1
                j_str = str(j).rjust(2, "0")
                path = os.path.join(self.__path, f"descripciones/{i}_{j_str}")
                os.mkdir(path)
                informacion = (
                    "descripcion",
                    "titulo",
                    "titulo_grafico",
                    "descripcion_grafico",
                    "fuente")
                for dato in informacion:
                    with open(os.path.join(path, dato + ".tex"), "w", encoding="utf-8") as f:
                        f.write(formato_LaTeX(sub_capitulo[dato]))
    
    def hacer_capitulos(self):
        for i, capitulo in enumerate(self.__data['capitulos']):
            i += 1
            file_name = capitulo["titulo"].replace(" ", "_")
            file_name = quitar_tildes(file_name)
            path = os.path.join(self.__path, f"tex/{file_name}.tex")
            sub_capitulos = capitulo["sub_capitulos"]
            with open(path, "w", encoding='utf-8') as f:
                for j, sub_capitulo in enumerate(sub_capitulos):
                    j += 1
                    j_str = str(j).rjust(2, "0")
                    carpeta = f"descripciones/{i}_{j_str}"
                    titulo =  sub_capitulo["titulo"]
                    if sub_capitulo["tipo_grafico"] in ("diagrama_tikz", "mapa_colorimetrico", "tabla_larga"):
                        f.write("\\cajota{%\n" + titulo + "}%\n")
                    else:
                        f.write("\\cajita{%\n" + titulo + "}%\n")

                    informacion = ("descripcion", "titulo_grafico", "descripcion_grafico")
                    for dato in informacion:
                        if sub_capitulo[dato] != "":
                            f.write("{%\n\\input{" + carpeta + "/" + dato + ".tex" + "}}%\n")
                        else:
                            f.write("{%\n}%\n")

                    if sub_capitulo["tipo_grafico"] in ("lineal", "barra", "columna"):
                        f.write("{%\n\\begin{tikzpicture}[x=1pt,y=1pt]\\input{" + f"graficas/{i}_{j_str}.tex" + "}\\end{tikzpicture}}%\n")
                    elif sub_capitulo["tipo_grafico"] == "mapa_colorimetrico":
                        f.write("{%\n\\includegraphics[scale=1]{" + f"graficas/{i}_{j_str}.pdf" + "}%\n")
                    elif sub_capitulo["tipo_grafico"] in ("tabla", "tabla_larga", "diagrama_tikz"):
                        f.write("{%\n\\input{" + f"graficas/{i}_{j_str}.tex" + "}}%\n")

                    f.write("{%\n\\input{" + carpeta + "/fuente.tex" + "}}%\n\n")

    def escribir_capitulo(self, capitulo, f: TextIOWrapper):
        titulo = capitulo["titulo"]
        file_name = titulo.replace(" ", "_") + ".tex"
        file_name = quitar_tildes(file_name)
        resumen = formato_LaTeX(capitulo["resumen"])
        f.write("\\INEchaptercarta{" + titulo + "}{" + resumen + "}\n")
        f.write("\\input{tex/" + file_name + "}\n")

    def hacer_portada(self):
        path = os.path.join(self.__path, f"tex/portada.tex")
        with open(path, 'w', encoding='utf-8') as f:
            mes = mes_by_ordinal(self.mes, abreviado=False)
            f.write("\\includepdf[pagecommand={\n")
            f.write("\\begin{tikzpicture}[remember picture, overlay]\n")
            f.write("\\node[nome] at ([yshift=2cm, xshift=1cm] current page) {\\color{white}{\\mgrande República de Guatemala:}};\n")
            f.write("\\node[nome] at ([yshift=0.3cm, xshift=1cm] current page) {\\color{white}{\\mgrande " + self.nombre_reporte + "}};\n")
            f.write("\\node[nome] at ([yshift=-1.4cm, xshift=1cm] current page) {\\color{white}{\\mgrande " + self.periodo + "}};\n")
            f.write("\\node at ([yshift=-12cm] current page) {\\color{white}{\\LARGE Guatemala, " + f"{mes.lower()} de {self.anio}" + "}};\n")
            f.write("\\end{tikzpicture}}\n")
            f.write("]{plantilla/portada.pdf}\n")

    def hacer_cuerpo(self):
        nombre = self.__data["nombre"].replace(" ", "_")
        nombre = quitar_tildes(nombre)
        path = os.path.join(self.__path, f"{nombre}.tex")
        with open(path, "w", encoding='utf-8') as f:
            f.write("\\input{plantilla/Carta3.tex}\n")
            f.write("\\renewcommand{\\partes}{No por favor}\n")
            f.write("\\renewcommand{\\titulodoc}{" + formato_LaTeX(self.__data["nombre"]) + "}\n")
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
            f.write("& Este documento fue elaborado empleando Python, {\\Sans R}, {\\Logos \\XeLaTeX} y Docker.\\\\\n")
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
            if self.__formulas:
                f.write("\\INEchaptercarta{Principales fórmulas de cálculo}{}\n")
                f.write("\\input{tex/formulas.tex}\n")
            for capitulo in self.__data["capitulos"]:
                if capitulo['anexo']:
                    self.escribir_capitulo(capitulo, f)
            f.write("\\includepdf{plantilla/contraportada.pdf}\n")
            f.write("\\end{document}\n")
            
    def compilar_reporte(self):
        nombre = self.__data["nombre"].replace(" ", "_")
        nombre = quitar_tildes(nombre)
        path = os.path.join(self.__path, f"{nombre}.tex")
        subprocess.run(
            f"cd {self.__path} && xelatex -synctex=1 -interaction=nonstopmode {path}",
            capture_output=True,
            text=True,
            shell=True
        )

    def crear_reporte(self):
        self.hacer_graficas()
        self.hacer_descripciones()
        self.hacer_capitulos()
        self.hacer_portada()
        self.hacer_cuerpo()
        # se ejecuta dos veces para que se actualicen los numeros de pagina
        # ademas de que se generan los indices y la tabla de contenidos
        self.compilar_reporte()
        self.compilar_reporte()
