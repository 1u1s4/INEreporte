##############################DESIGUALDAD#########################################
library(funcionesINE)
library(xlsx)
library(xlsxjars)
documento <- leerLibroNormal('/mnt/datos/GitHub/ResultadosEncovi/Libros/32- Desigualdad 1151115.xlsx')
escribirCSV(documento, ruta = '/mnt/datos/GitHub/ResultadosEncovi/CSVENCOVI/')
desigualdad <- leerLibro(ruta = '/mnt/datos/GitHub/ResultadosEncovi/Libros/desigualdadCSV.xlsx')
escribirCSV(lista = desigualdad, ruta = '/mnt/datos/GitHub/ResultadosEncovi/CSV/2/')
anual()
ENC2<- cargaMasiva("/mnt/datos/GitHub/ResultadosEncovi/CSV/2/")

g1<- graficaLinea(ENC2$"2_01",rotar = "h", precision = 2,inicio = 0.2, final = 0.7)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/2_01.tex",g1)

g2<- graficaLinea(ENC2$"2_02",rotar = "h",  precision = 2,inicio = 0.25, final = 0.55)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/2_02.tex",g2)

g3<- graficaLinea(ENC2$"2_03",rotar = "h",  precision = 2, inicio = 0.35, final = 0.95)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/2_03.tex",g3)

g4<- graficaLinea(ENC2$"2_04",rotar = "h",  precision = 2,inicio = 0.3, final = 0.8)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/2_04.tex",g4)

g5<- graficaLinea(ENC2$"2_05",rotar = "h", inicio = 0, final = 4)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/2_05.tex",g5)

g6<- graficaLinea(ENC2$"2_06",rotar = "h", inicio = 40, final = 65)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/2_06.tex",g6)

g7<- graficaLinea(ENC2$"2_07",rotar = "h", inicio = 10, final = 35)
exportarLatex("/mnt/datos/GitHub/ResultadosEncovi/graficas/2_07.tex",g7)
