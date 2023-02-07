from reporteine import ReporteINE
from time import time
from datosipc import datosIPC
from funcionesjo import mes_by_ordinal

if __name__ == "__main__":
    t = time()
    mes = 1
    anio = 2023
    mes_ = mes_by_ordinal(mes, abreviado=False).capitalize()
    fecha = f"{mes_} {anio}"
    datos = datosIPC(anio, mes)
    reporte = ReporteINE("Prueba_IPC", anio, mes)
# capitulo 1
    reporte.presentacion(datos.introduccion())
    reporte.agregar_capitulo(
        titulo="Detalle del operativo de campo del IPC"
    )
    subcap_data = datos.serie_fuentes()
    reporte.agregar_subcapitulo(
        titulo="Cobertura de fuentes",
        titulo_grafico="Histórico de cobertura de fuentes",
        descripcion_grafico="República de Guatemala, serie histórica, cantidad de fuentes",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico=dict(Q4Etiquetas=True)
    )
    subcap_data = datos.serie_precios(Qcobertura=True)
    reporte.agregar_subcapitulo(
        titulo="Cobertura de precios",
        titulo_grafico="Histórico de cobertura de precios",
        descripcion_grafico="República de Guatemala, serie histórica, cantidad de precios",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico=dict(Q4Etiquetas=True)
    )
    subcap_data = datos.serie_precios(Qcobertura=False)
    reporte.agregar_subcapitulo(
        titulo="Imputación de precios",
        titulo_grafico="Histórico de imputación de precios",
        descripcion_grafico="República de Guatemala, serie histórica, porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="columna",
        data=subcap_data[0],
        opciones_grafico={}
    )
    subcap_data = datos.desagregacion_fuentes()
    reporte.agregar_subcapitulo(
        titulo="Desagregación de fuentes",
        titulo_grafico="Desagregación de fuentes por tipo",
        descripcion_grafico=f"República de Guatemala, {fecha}, porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="barra",
        data=subcap_data[0],
        opciones_grafico={"precision":2}
    )
# capitulo 2
    reporte.agregar_capitulo(
        titulo="Variables exógenas"
    )
    subcap_data = datos.indice_precio_alimentos()
    reporte.agregar_subcapitulo(
        titulo="Precio internacional de los alimentos",
        titulo_grafico="Índice de precios de los alimentos de la FAO",
        descripcion_grafico="Indicador internacional, serie histórica, adimensional",
        descripcion=subcap_data[1],
        fuente="FAO",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.petroleo()
    reporte.agregar_subcapitulo(
        titulo="Precio del pretróleo",
        titulo_grafico="Precio promedio mensual del barril del petróleo",
        descripcion_grafico="Indicador internacional, serie histórica, en dólares por barril",
        descripcion=subcap_data[1],
        fuente="Federal Reserve Economic Data",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.cambio_quetzal()
    reporte.agregar_subcapitulo(
        titulo="Cambio del quetzal",
        titulo_grafico="Tipo de cambio nominal promedio",
        descripcion_grafico="República de Guatemala, serie histórica, en quetzales por dólar estadounidense",
        descripcion=subcap_data[1],
        fuente="Banco de Guatemala",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.tasa_interes()
    reporte.agregar_subcapitulo(
        titulo="Tasa de interés",
        titulo_grafico="Tasas de interés activa bancaria",
        descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="Banco de Guatemala",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = ((('Dic-2021', 7.096542338), ('Ene-2022', 7.5259344012204465), ('Feb-2022', 7.912024484898206), ('Mar-2022', 8.557586368232784), ('Abr-2022', 8.224139288485999), ('May-2022', 8.516412942713858), ('Jun-2022', 8.995220608588127), ('Jul-2022', 8.482129735766986), ('Ago-2022', 8.24923469014105), ('Sep-2022', 8.222410234342536), ('Oct-2022', 7.76311508008245), ('Nov-2022', 7.117878531114008), ('Dic-2022', 6.420682121616728)), 'El Índice de Precios al Consumidor en los Estados Unidos de América\\footnote{Para mayor información sobre el indice de precios al consumidor de los Estados Unidos, visite \\url{http://www.bls.gov/cpi}.} registró una variación interanual al mes de diciembre 2022 de 6.42%. En diciembre 2021 la variación interanual se ubicó en 7.10%, por lo que este indicador se desaceleró 0.68 puntos porcentuales en el último año.')
    reporte.agregar_subcapitulo(
        titulo="Índice de Precios al Consumidor de EE.UU.",
        titulo_grafico="Variación interanual del IPC de Estados Unidos de América",
        descripcion_grafico="Estados Unidos de América, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="FRED",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )



    print(f"Generacion de datos [{time()-t:.2f} s]")
    reporte.crear_reporte()
    #reporte.compilar_reporte()
    tf = time()
    print(f"[{(tf-t)//60:.2f} min]")