##############################OBJETIVOS DEL MILENIO#########################################
library(funcionesINE)
library(xlsx)
library(xlsxjars)
odm <- leerLibroNormal('/mnt/datos/GitHub/ResultadosEncovi/Libros/odmCocinado.xlsx')
escribirCSV(odm, ruta = '/mnt/datos/GitHub/ResultadosEncovi/CSVENCOVI/')
odmCSV <- leerLibro(ruta = '/mnt/datos/GitHub/ResultadosEncovi/Libros/odmCSV.xlsx')
escribirCSV(lista = odmCSV, ruta = '/mnt/datos/GitHub/ResultadosEncovi/CSV/3/')
anual()
ENC3<- cargaMasiva("/mnt/datos/GitHub/ResultadosEncovi/CSV/3")

g1<- graficaLinea(ENC3$'3_01',rotar = "h", precision = 1, final = 28, inicio = 0) 
exportarLatex('/mnt/datos/GitHub/ResultadosEncovi/graficas/3_01.tex', g1)  

g2<- graficaCol(ENC3$"3_02", ordenar = F)
g2 <- etiquetasHorizontales(g2)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/3_02.tex", g2)

g4<- graficaLinea(ENC3$'3_04',rotar = "h", precision = 1, inicio= 1, final = 8) 
exportarLatex('/mnt/datos/GitHub/ResultadosEncovi/graficas/3_04.tex', g4)  

g5 <- graficaCol(ENC3$"3_05")
g5 <- etiquetasHorizontales(g2)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/3_05.tex", g5)


g5<- graficaCol(ENC3$"3_05", ordenar = F)
g5 <- etiquetasHorizontales(g5)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/3_05.tex",g5)






g7<- graficaLinea(ENC3$'3_07',rotar = "h", precision = 1, final = 70, inicio = 50 ) 
exportarLatex('/mnt/datos/GitHub/ResultadosEncovi/graficas/3_07.tex', g7)  

g8<- graficaCol(ENC3$"3_08", ordenar = F)
g8 <- etiquetasHorizontales(g8)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/3_08.tex",g8)


g10<- graficaLinea(ENC3$'3_10',rotar = "h", precision = 2) 
exportarLatex('/mnt/datos/GitHub/ResultadosEncovi/graficas/3_10.tex', g10)  

g11<- graficaCol(ENC3$"3_11", ordenar = F)
g11 <- etiquetasHorizontales(g11)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/3_11.tex",g11)


g12<- graficaCol(ENC3$"3_12", ordenar = F)
g12 <- etiquetasHorizontales(g12)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/3_12.tex",g12)


g13<- graficaLinea(ENC3$'3_13',rotar = "h", precision = 2) 
exportarLatex('/mnt/datos/GitHub/ResultadosEncovi/graficas/3_13.tex', g13)  


g14<- graficaCol(ENC3$"3_14", ordenar = F)
g14 <- etiquetasHorizontales(g14)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/3_14.tex",g14)

g16<- graficaLinea(ENC3$'3_16',rotar = "h", precision = 2, inicio = 30, final = 60) 
exportarLatex('/mnt/datos/GitHub/ResultadosEncovi/graficas/3_16.tex', g16)  


g17<- graficaCol(ENC3$"3_17", ordenar = F)
g17 <- etiquetasHorizontales(g17)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/3_17.tex",g17)

g19<- graficaLinea(ENC3$"3_19",rotar = "h", inicio = 0, final = 90)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/3_19.tex",g19)

g20<- graficaCol(ENC3$"3_20", ordenar = F)
g20 <- etiquetasHorizontales(g20)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/3_20.tex",g20)

g22<- graficaLinea(ENC3$"3_22",rotar = "h", inicio = 0, final = 95)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/3_22.tex",g22)

g23<- graficaCol(ENC3$"3_23", ordenar = F)
g23 <- etiquetasHorizontales(g23)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/3_23.tex",g23)

g25<- graficaLinea(ENC3$"3_25",rotar = "h", inicio = 40, final= 90)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/3_25.tex",g25)

g26<- graficaCol(ENC3$"3_26", ordenar = F)
g26 <- etiquetasHorizontales(g26)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/3_26.tex",g26)

g28<- graficaLinea(ENC3$"3_28",rotar = "h",inicio = 15, final = 80)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/3_28.tex",g28)

g29<- graficaCol(ENC3$"3_29", ordenar = F)
g29 <- etiquetasHorizontales(g29)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/3_29.tex",g29)




