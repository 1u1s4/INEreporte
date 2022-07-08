library(funcionesINE)
anual(rgb(0,0,1), rgb(0.6156862745098039,0.7333333333333333,1))
CSVrute <- "C:/Users/laalvarado/Documents/GitHub/INE_LaTeX/Plantilla/ResultadosEncovi/CSV/1"
TEXrute <- "C:/Users/laalvarado/Documents"
ENC1<- cargaMasiva(CSVrute)


#g1<- graficaDobleLinea(ENC1$"1.1",ruta = "C:/Users/INE/Desktop/arregladaENCOVI_2014/1_01.tex")
g1<- graficaLinea(ENC1$"1_01",rotar = "h")##cAMBIAR
exportarLatex(paste(TEXrute, "/1_01.tex"), g1)

g2<- graficaLinea(ENC1$"1.2",rotar = "h")
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/1_02.tex",g2)

g4<- graficaColCategorias(ENC1$"1.3",etiquetasCategorias = "A",
                          ruta = "C:/Users/INE/Desktop/arregladaENCOVI_2014/1_03.tex",etiquetas = "h")

g5<- graficaColCategorias(ENC1$"1.4",etiquetasCategorias = "A",
                          ruta = "C:/Users/INE/Desktop/arregladaENCOVI_2014/1_04.tex",etiquetas = "h")

##g5 mapa


g11<- graficaLinea(ENC1$"1.6",rotar = "h")
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/1_06.tex",g11)


g3<- graficaLinea(ENC1$"1.7",rotar = "h")
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/1_07.tex",g3)


g6<- graficaColCategorias(ENC1$"1.8",etiquetasCategorias = "A",
                          ruta = "C:/Users/INE/Desktop/arregladaENCOVI_2014/1_08.tex",etiquetas = "h")

g7<- graficaColCategorias(ENC1$"1.9",etiquetasCategorias = "A",
      ruta = "C:/Users/INE/Desktop/arregladaENCOVI_2014/1_09.tex",etiquetas = "h")

##g10 mapa


g8<- graficaLinea(ENC1$"1.11",rotar = "h")
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/1_11.tex",g8)

g9<- graficaLinea(ENC1$"1.12",rotar = "h")
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/1_12.tex",g9)

#g13 mapa

g10<- graficaLinea(ENC1$"1.14",rotar = "h")
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/1_14.tex",g10)

#g15 mapa


rm(list = ls())

ENC2<- cargaMasiva("C:/Users/INE/Desktop/arregladaENCOVI_2014/CSV/2")
g1<- graficaLinea(ENC2$"2.1",rotar = "h", precision = 3)
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/2_01.tex",g1)
g2<- graficaLinea(ENC2$"2.2",rotar = "h",  precision = 3)
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/2_02.tex",g2)
g3<- graficaLinea(ENC2$"2.3",rotar = "h",  precision = 3)
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/2_03.tex",g3)
g4<- graficaLinea(ENC2$"2.4",rotar = "h",  precision = 3)
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/2_04.tex",g4)
g5<- graficaLinea(ENC2$"2.5",rotar = "h")
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/2_05.tex",g5)
g6<- graficaLinea(ENC2$"2.6",rotar = "h")
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/2_06.tex",g6)
g7<- graficaLinea(ENC2$"2.7",rotar = "h")
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/2_07.tex",g7)

## g8 mapa
## g9 mapa
## g10 mapa
## g11 mapa
## g12 mapa




rm(list = ls())
ENC3<- cargaMasiva("C:/Users/INE/Desktop/arregladaENCOVI_2014/CSV/3")



### esta va en forma de pir?mide
# g1<- graficaCol(ENC3$"3.1")
# g1 <- etiquetasHorizontales(g1)
# exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/3_01.tex",g1)

g1<- graficaColCategorias(ENC3$"3.1",etiquetasCategorias = "A",
                          ruta = "C:/Users/INE/Desktop/arregladaENCOVI_2014/3_01.tex",etiquetas = "h")



g2<- graficaColCategorias(ENC3$"3.2",etiquetasCategorias = "A",
                  ruta = "C:/Users/INE/Desktop/arregladaENCOVI_2014/3_02.tex",etiquetas = "h")

# g3<- graficaColCategorias(ENC3$"3.3",etiquetasCategorias = "A",
#                           ruta = "C:/Users/INE/Desktop/arregladaENCOVI_2014/3_03.tex",etiquetas = "h")
# g4<- graficaColCategorias(ENC3$"3.4",etiquetasCategorias = "A",
#                           ruta = "C:/Users/INE/Desktop/arregladaENCOVI_2014/3_04.tex",etiquetas = "h")

g5<- graficaCol(ENC3$"3.5", ordenar = F)
g5 <- etiquetasHorizontales(g5)
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/3_05.tex",g5)

# g6<- graficaCol(ENC3$"3.6")
# g6 <- etiquetasHorizontales(g6)
# exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/3_06.tex",g6)


# g7<- graficaCol(ENC3$"3.7")
# g7 <- etiquetasHorizontales(g7)
# exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/3_07.tex",g7)


g8<- graficaColCategorias(ENC3$"3.8",etiquetasCategorias = "A", ancho = 0.6,
                          ruta = "C:/Users/INE/Desktop/arregladaENCOVI_2014/3_08.tex",etiquetas = "h")

g9<- graficaColCategorias(ENC3$"3.9",etiquetasCategorias = "A", ancho = 0.6,
                ruta = "C:/Users/INE/Desktop/arregladaENCOVI_2014/3_09.tex",etiquetas = "h")

g10<- graficaCol(ENC3$"3.10", ordenar = F)
g10 <- etiquetasHorizontales(g10)
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/3_10.tex",g10)


g11<- graficaCol(ENC3$"3.11", ordenar = F, ancho = 0.5)
g11 <- etiquetasHorizontales(g11)
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/3_11.tex",g11)


g12<- graficaCol(ENC3$"3.12", ordenar = F)
g12 <- etiquetasHorizontales(g12)
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/3_12.tex",g12)


g13<- graficaColCategorias(ENC3$"3.13",etiquetasCategorias = "A", ancho = 0.6,
                          ruta = "C:/Users/INE/Desktop/arregladaENCOVI_2014/3_13.tex",etiquetas = "h")



g14<- graficaCol(ENC3$"3.14", ordenar = F)
g14 <- etiquetasHorizontales(g14)
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/3_14.tex",g14)


#g14<- graficaLinea(ENC3$"3.14",rotar = "h")
#exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/3_14.tex",g14)

g15<- graficaCol(ENC3$"3.15", ordenar = F)
g15 <- etiquetasHorizontales(g15)
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/3_15.tex",g15)

g16<- graficaCol(ENC3$"3.16", ordenar = F)
g16 <- etiquetasHorizontales(g16)
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/3_16.tex",g16)


g17<- graficaBar(ENC3$"3.17")
g17 <- etiquetasBarras(g17)
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/3_17.tex",g17)

g18<- graficaLinea(ENC3$"3.18",rotar = "h")
exportarLatex("C:/Users/INE/Desktop/arregladaENCOVI_2014/3_18.tex",g18)


### g19 ese mapa

