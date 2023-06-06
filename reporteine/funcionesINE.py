import os

import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages
import pandas as pd
from rpy2.robjects import pandas2ri
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
        r_data = pandas2ri.py2rpy(data)  # Convierte el DataFrame de pandas a un objeto R
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
        r_data = pandas2ri.py2rpy(data)  # Convierte el DataFrame de pandas a un objeto R
        if self.Qanual:
            self.__funcionesINE.anual(
                robjects.r("rgb(0,0,1)"),
                robjects.r("rgb(0.6156862745098039,0.7333333333333333,1)")
            )
        if ordenar:
            ordenar = robjects.r("TRUE")
        else:
            ordenar = robjects.r("FALSE")
        g = self.__funcionesINE.graficaBar(
                    r_data,
                    ancho=ancho,
                    ordenar=ordenar,
                    escala=escala
                )
        g =  self.__funcionesINE.etiquetasBarras(
                g,
                precision=precision
            )
        self.__funcionesINE.exportarLatex(
            ruta_salida + f"/{nombre}.tex",
            g
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
        r_data = pandas2ri.py2rpy(data)  # Convierte el DataFrame de pandas a un objeto R
        if self.Qanual:
            self.__funcionesINE.anual(
                robjects.r("rgb(0,0,1)"),
                robjects.r("rgb(0.6156862745098039,0.7333333333333333,1)")
            )
        if ordenar:
            ordenar = robjects.r("TRUE")
        else:
            ordenar = robjects.r("FALSE")
        g = self.__funcionesINE.graficaCol(
                    r_data,
                    ancho=ancho,
                    ordenar=ordenar,
                    escala=escala
                )
        g =  self.__funcionesINE.etiquetasHorizontales(
                g,
                precision=precision
            )
        g = self.__funcionesINE.rotarEtiX(g)
        self.__funcionesINE.exportarLatex(
            ruta_salida + f"/{nombre}.tex",
            g
        )