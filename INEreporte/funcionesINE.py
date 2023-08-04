import os

import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages
import pandas as pd
from rpy2.robjects import pandas2ri
import rpy2.rinterface_lib.callbacks
import logging

# Configuramos un manejador de registro para ignorar los mensajes de R.
rpy2.rinterface_lib.callbacks.logger.setLevel(logging.ERROR)

pandas2ri.activate()

class FuncionesINE:
    def __init__(self, r_home: str = None) -> None:
        if r_home:
            os.environ["R_HOME"] = r_home
        self.__funcionesINE = rpackages.importr('funcionesINE')
        self.Qanual = True

    def graficaLinea(
        self,
        data: pd.DataFrame,
        ruta_salida: str,
        nombre: str,
        inicio: int = -1,
        ancho: float = 1.5,
        precision: int = 1,
        escala: str = "normal",
        rotar: bool = True,
        final = None,
        etiquetaCadaSeis: bool = False,
        Q4Etiquetas: bool = False) -> None:
        # Convierte el DataFrame de pandas a un objeto R
        r_data = pandas2ri.py2rpy(data)
        if self.Qanual:
            self.__funcionesINE.anual(
                robjects.r("rgb(0,0,1)"),
                robjects.r("rgb(0.6156862745098039,0.7333333333333333,1)")
            )
        if Q4Etiquetas:
            self.__funcionesINE.cuatroEtiquetas()
        rotar = robjects.r("TRUE") if rotar else robjects.r("FALSE")
        etiquetaCadaSeis = robjects.r("TRUE") if etiquetaCadaSeis else robjects.r("FALSE")
        if final is None:
            final = robjects.r("NA")
        self.__funcionesINE.exportarLatex(
            ruta_salida + f"/{nombre}.tex",
            self.__funcionesINE.graficaLinea(
                r_data,
                inicio=inicio,
                ancho=ancho,
                precision=precision,
                escala=escala,
                rotar=rotar,
                final=final,
                etiquetaCadaSeis=etiquetaCadaSeis
            )
        )

    def graficaBar(
        self,
        data: pd.DataFrame,
        ruta_salida: str,
        nombre: str,
        precision: int = 2,
        ancho: float = 0.6,
        ordenar: bool = True,
        escala = 'normal') -> None:
        # Convierte el DataFrame de pandas a un objeto R
        r_data = pandas2ri.py2rpy(data)
        if self.Qanual:
            self.__funcionesINE.anual(
                robjects.r("rgb(0,0,1)"),
                robjects.r("rgb(0.6156862745098039,0.7333333333333333,1)")
            )
        if ordenar:
            ordenar = robjects.r("TRUE")
        else:
            ordenar = robjects.r("FALSE")
        grafica = self.__funcionesINE.graficaBar(
                    r_data,
                    ancho=ancho,
                    ordenar=ordenar,
                    escala=escala
                )
        grafica =  self.__funcionesINE.etiquetasBarras(
                grafica,
                precision=precision
            )
        self.__funcionesINE.exportarLatex(
            ruta_salida + f"/{nombre}.tex",
            grafica
        )

    def graficaCol(
        self,
        data: pd.DataFrame,
        ruta_salida: str,
        nombre: str,
        precision: int = 2,
        ancho: float = 0.6,
        ordenar: bool = False,
        escala = 'normal') -> None:
        # Convierte el DataFrame de pandas a un objeto R
        r_data = pandas2ri.py2rpy(data)
        if self.Qanual:
            self.__funcionesINE.anual(
                robjects.r("rgb(0,0,1)"),
                robjects.r("rgb(0.6156862745098039,0.7333333333333333,1)")
            )
        if ordenar:
            ordenar = robjects.r("TRUE")
        else:
            ordenar = robjects.r("FALSE")
        grafica = self.__funcionesINE.graficaCol(
                    r_data,
                    ancho=ancho,
                    ordenar=ordenar,
                    escala=escala
                )
        grafica =  self.__funcionesINE.etiquetasHorizontales(
                grafica,
                precision=precision
            )
        grafica = self.__funcionesINE.rotarEtiX(grafica)
        self.__funcionesINE.exportarLatex(
            ruta_salida + f"/{nombre}.tex",
            grafica
        )

    def tabla_LaTeX(
        self,
        datos,
        ruta_salida,
        nombre,
        precision: int = 2,
        tabla_inflacion: bool = False):
        with open(os.path.join(ruta_salida, f"{nombre}.tex"), "w", encoding="utf-8") as file:
            file.write("\\setlength{\\arrayrulewidth}{1.5pt}\n")
            file.write("\\definecolor{Fcolor}{HTML}{e5e5fa}\n")
            file.write("\\definecolor{Lcolor}{HTML}{4d80ff}\n")
            # si es tabla de inflacion lleva esa cosa sobre los meses de "Inflacion interanual a"
            if tabla_inflacion:
                file.write("\\setlength{\\aboverulesep}{-1pt}\n")
                file.write("\\setlength{\\belowrulesep}{0pt}\n")
            alinacion = len(datos[0])*"c"
            file.write("\\begin{tabular}{" + alinacion + "}\n")
            file.write("\\arrayrulecolor{Lcolor} \hline\n")
            # si es tabla de inflacion lleva esa cosa sobre los meses de "Inflacion interanual a"
            if tabla_inflacion:
                file.write("\\rowcolor{Fcolor} & \\multicolumn{2}{c}{\\textbf{Inflacion interanual a}}\\\\\n")
                file.write("\\cmidrule[0.9pt]{2-3}\n")
            file.write("\\rowcolor{Fcolor} ")
            i = 0
            for encabezado in datos[0]:
                i += 1
                file.write("\\textbf{" + encabezado + "}")
                if i != len(datos[0]):
                    file.write(" & ")
                else:
                    file.write("\\\\\n")
            file.write("\\hline\n")
            file.write("\\rowcolor{white} ")
            for i in range(1, len(datos)):
                j = 0
                for celda in datos[i]:
                    j += 1
                    if type(celda) is str:
                        file.write(f"{celda}")
                    else:
                        file.write(f"{float(celda):.{precision}f}")
                    if j != len(datos[i]):
                        file.write(" & ")
                    else:
                        file.write("\\\\\n")
            file.write("\\hline\n")
            file.write("\\end{tabular}\n")

    '''
    def export_to_longtable(
            self,
            df: pd.DataFrame,
            filename: str,
            ruta_salida: str,
            header: bool=True,
            decimals: int=2):
        """
        Exporta un dataframe a un longtable de LaTeX en un archivo.
        
        Parameters:
        df (pandas.DataFrame): DataFrame a exportar.
        filename (str): Nombre del archivo a guardar.
        caption (str): Leyenda de la tabla.
        column_format (str): Cadena que describe el formato de las columnas.
        header (bool): Si True, muestra el encabezado de la tabla.
        decimals (int): Cantidad de decimales para los números. Si el valor no es numérico, se muestra tal cual.
        """
        with open(f"{ruta_salida}/{filename}.tex", 'w', encoding="utf-8") as f:
            f.write('\\begin{longtable}{' + 'c'*len(df.columns) + '}\n')
            f.write('\\toprule\n')
            
            # Escribir el encabezado
            if header:
                f.write(' & '.join([col.replace('_', '\\_') for col in df.columns]))
                f.write('\\\\\\midrule\n')
            
            f.write('\\endfirsthead\n')
            f.write('\\multicolumn{' + str(len(df.columns)) + '}{c}{{\\bfseries \\tablename\\ \\thetable{} -- '
                    'Continuación de la página anterior}}\\\\\n')
            f.write('\\toprule\n')
            if header:
                f.write(' & '.join([col.replace('_', '\\_') for col in df.columns]))
                f.write('\\\\\\midrule\n')
            f.write('\\endhead\n')
            f.write('\\midrule\n')
            f.write('\\multicolumn{' + str(len(df.columns)) + '}{r}{{Continúa en la siguiente página}}\\\\\n')
            f.write('\\endfoot\n')
            f.write('\\bottomrule\n')
            f.write('\\endlastfoot\n')
            
            # Escribir los datos
            import re
            for _, row in df.iterrows():
                values = []
                for value in row:
                    if pd.isna(value):
                        values.append('')
                    elif isinstance(value, (int, float)):
                        valor = round(value, decimals)
                        if re.match(r"^[-]0\.0*$", str(valor)):
                            valor = int(valor)
                        valor = '{:.{}f}'.format(valor, decimals)
                        values.append(valor)
                    else:
                        values.append(str(value))
                f.write(' & '.join(values))
                f.write('\\\\\n')
            
            f.write('\\end{longtable}\n')
        '''
