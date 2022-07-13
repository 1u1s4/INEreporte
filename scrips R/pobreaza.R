library(funcionesINE)
library(xlsx)
library(rJava)
library(xlsxjars)
rutaRaiz <- 'C:/Users/laalvarado/Documents/pruebas/'
rutaSalidaCSV <- paste(rutaRaiz, "CSV/1", sep="")
rutaSalidaTex <- paste(rutaRaiz, "graficas/", sep="")
rutaCocinado <- paste(rutaRaiz, "Libros/pobrezaCocinado.xlsx", sep="")
rutaSalidaCocinado <- paste(rutaRaiz, "CSVENCOVI/", sep="")
rutaLibro <- paste(rutaRaiz, "Libros/pobrezaCSV.xlsx", sep="")

pobreza <- leerLibroNormal(rutaCocinado)
escribirCSV(pobreza, ruta=rutaSalidaCocinado)

pobrezaCSV <- leerLibro(ruta=rutaLibro)
escribirCSV(lista=pobrezaCSV, ruta=rutaSalidaCSV)

anual()

ENC1 <- cargaMasiva(rutaSalidaCSV, codificacion='utf8')

rutaTex <- function(fileName){
  return(paste(rutaSalidaTex, fileName, sep=""))
}

g1 <- graficaLinea(ENC1$"1_01", rotar="h", inicio=0, final=12000)
exportarLatex(rutaTex("1_01.tex"), g1)

g2 <- graficaLinea(ENC1$"1_02", rotar="h", inicio=20, final=63)
exportarLatex(rutaTex("1_02.tex"), g2)

g3 <- graficaColCategorias(ENC1$"1_03", ancho=0.6, etiquetasCategorias="A", ruta=rutaTex("1_03.tex"), etiquetas="h")

g4 <- graficaColCategorias(ENC1$"1_04", ancho=0.6, etiquetasCategorias="A",ruta=rutaTex("1_04.tex"), etiquetas="h")

g8 <- graficaLinea(ENC1$"1_08",rotar = "h", inicio=0, final=7000)
exportarLatex(rutaTex("1_08.tex"), g8)

g9 <- graficaLinea(ENC1$"1_09", rotar="h", inicio=0, final=27)
exportarLatex(rutaTex("1_09.tex"), g9)

g10 <- graficaColCategorias(ENC1$"1_10", ancho=0.6, etiquetasCategorias="A", ruta=rutaTex("1_10.tex"), etiquetas="h")

g11 <- graficaColCategorias(ENC1$"1_11", ancho=0.6, etiquetasCategorias="A", ruta=rutaTex("1_11.tex"), etiquetas="h")

g13 <- graficaLinea(ENC1$"1_13", rotar="h", inicio=0, final=26)
exportarLatex(rutaTex("1_13.tex"), g13)

g14 <- graficaLinea(ENC1$"1_14", rotar="h", inicio=0, final=7)
exportarLatex(rutaTex("1_14.tex"), g14)

g15 <- graficaLinea(ENC1$"1_15", rotar="h", inicio=0, final=15)
exportarLatex(rutaTex("1_15.tex"), g15)

g16 <- graficaLinea(ENC1$"1_16", rotar="h", inicio=0, final=15)
exportarLatex(rutaTex("1_16.tex"), g16)

g18 <- graficaCol(ENC1$"1_18", ordenar=F)
g18 <- etiquetasHorizontales(g18)
exportarLatex(rutaTex("1_18.tex"), g18)