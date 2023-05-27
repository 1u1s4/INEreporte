import os

import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages


class FuncionesINE:
    def __init__(self, r_home: str = r"C:\Program Files\R\R-4.2.2") -> None:
        os.environ["R_HOME"] = r_home
        #devtools = rpackages.importr('devtools')
        #devtools.install_github("1u1s4/funcionesINE", ref="luis-dev", upgrade="never")
        self.__funcionesINE = rpackages.importr('funcionesINE')
        self.__datos = list
        self.Qanual = True

    def cargaMasiva(self, csv_path: str) -> None:
        self.__datos = self.__funcionesINE.cargaMasiva(csv_path, codificacion='UTF8')

    def escribirCSV(self, ruta_libro: str, ruta_salida: str) -> None:
        self.__funcionesINE.escribirCSV(
            lista=self.__funcionesINE.leerLibro(ruta=ruta_libro),
            ruta=ruta_salida
            )

    def escribirCSVcocinado(self, ruta_libro: str, ruta_salida: str) -> None:
        self.__funcionesINE.escribirCSV(
            lista=self.__funcionesINE.leerLibroNormal(ruta=ruta_libro),
            ruta=ruta_salida
            )

    def graficaLinea(
        self,
        data_index: int,
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
                self.__datos.rx(data_index)[0],
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
        data_index: int,
        ruta_salida: str,
        nombre: str,
        precision: int = 2,
        ancho: float = 0.6,
        ordenar: bool = True,
        escala = 'normal') -> None:
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
                    self.__datos.rx(data_index)[0],
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
        data_index: int,
        ruta_salida: str,
        nombre: str,
        precision: int = 2,
        ancho: float = 0.6,
        ordenar: bool = False,
        escala = 'normal') -> None:
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
                    self.__datos.rx(data_index)[0],
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