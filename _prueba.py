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
    subcap_data = datos.ipc_usa()
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

    subcap_data = datos.ipc_mex()
    reporte.agregar_subcapitulo(
        titulo="Índice de Precios al Consumidor de México",
        titulo_grafico="Variación interanual del IPC de México",
        descripcion_grafico="Estados Unidos Mexicanos, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="FRED",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    """
    subcap_data = datos.inflacion_CA_RD_MEX()
    reporte.agregar_subcapitulo(
        titulo="Inflación en Centro América, República Dominicana y México",
        titulo_grafico="Tasa de variación interanual del IPC de los países Centroamericanos, República Dominicana y México",
        descripcion_grafico="Centro América, República Dominicana y México, meses seleccionados, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="tabla",
        data=subcap_data[0],
        opciones_grafico={"precision":2}
    )
    """

    print(f"Generacion de datos [{time()-t:.2f} s]")
    reporte.crear_reporte()
    #reporte.compilar_reporte()
    tf = time()
    print(f"[{(tf-t)//60:.2f} min]")