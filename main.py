from time import time

from datosipc import datosIPC

from funcionesjo import mes_by_ordinal
from reporteine import ReporteINE

if __name__ == "__main__":
    t = time()
    mes = 4
    anio = 2023
    mes_ = mes_by_ordinal(mes, abreviado=False).capitalize()
    fecha = f"{mes_} {anio}"
    datos = datosIPC(anio, mes, dbBackup=True)
    print(f"Generacion de datos [{time()-t:.2f} s]")
    reporte = ReporteINE("Índice de Precios al Consumidor", anio, mes)
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
    subcap_data = datos.serie_precios()
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
    subcap_data_imputacion = list(datos.serie_imputacion())
    eliminar = subcap_data_imputacion[0][-1]
    subcap_data_imputacion[0].remove(eliminar)
    subcap_data_imputacion[0].append(('Abr-2023', 1.60))
    subcap_data_imputacion[1] = 'El porcentaje de precios imputados en abril 2023 es de 1.60%. El mayor porcentaje de imputaciones fue en el mes de octubre 2022 con una cantidad de 5.28% y el menor se encuentra en el mes de abril 2023 con una cantidad de 1.60%.'
    subcap_data = subcap_data_imputacion
    reporte.agregar_subcapitulo(
        titulo="Imputación de precios",
        titulo_grafico="Histórico de imputación de precios",
        descripcion_grafico="República de Guatemala, serie histórica, porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="columna",
        data=subcap_data[0],
        opciones_grafico={"precision":1}
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
        opciones_grafico={"precision":1}
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
# capitulo 3
    reporte.agregar_capitulo(
        titulo="Resultados del IPC"
    )
    subcap_data = datos.serie_IPC(0)
    reporte.agregar_subcapitulo(
        titulo="Evolución del IPC",
        titulo_grafico="IPC, base diciembre del 2010",
        descripcion_grafico="República de Guatemala, serie histórica, adimensional",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.serie_inflacion(0, 'interanual')
    reporte.agregar_subcapitulo(
        titulo="Evolución del cambio anual del IPC (Ritmo Inflacionario)",
        titulo_grafico="Variación interanual del IPC",
        descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.serie_inflacion(0, 'acumulada')
    reporte.agregar_subcapitulo(
        titulo="Evolución de la variación acumulada del IPC",
        titulo_grafico="Variación acumulada del IPC",
        descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="columna",
        data=subcap_data[0],
        opciones_grafico={}
    )
    subcap_data = datos.serie_inflacion(0, 'intermensual')
    reporte.agregar_subcapitulo(
        titulo="Evolución de la variación mensual del IPC",
        titulo_grafico="Variación intermensual del IPC",
        descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.incidencias_divisiones(0)
    reporte.agregar_subcapitulo(
        titulo="Incidencias mensuales por división de gasto básico",
        titulo_grafico="Incidencias mensuales",
        descripcion_grafico=f"República de Guatemala, {fecha}, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="barra",
        data=subcap_data[0],
        opciones_grafico={"precision":2}
    )
    subcap_data = datos.incidencias_gba(0, True)
    reporte.agregar_subcapitulo(
        titulo="Gastos básicos con mayor impacto positivo en la variación mensual",
        titulo_grafico="Gastos básicos con mayor incidencia positiva",
        descripcion_grafico=f"República de Guatemala, {fecha}, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="barra",
        data=subcap_data[0],
        opciones_grafico={"precision":2}
    )
    subcap_data = datos.incidencias_gba(0, False)
    reporte.agregar_subcapitulo(
        titulo="Gastos básicos con mayor impacto negativo en la variación mensual",
        titulo_grafico="Gastos básicos con mayor incidencia negativa",
        descripcion_grafico=f"República de Guatemala, {fecha}, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="barra",
        data=subcap_data[0],
        opciones_grafico={"precision":2}
    )
    subcap_data = datos.serie_poder_adquisitivo(0)
    reporte.agregar_subcapitulo(
        titulo="Valor del Quetzal",
        titulo_grafico="Poder adquisitivo del quetzal",
        descripcion_grafico="República de Guatemala, serie histórica, adimensional",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.serie_historica("mensual")
    reporte.agregar_subcapitulo(
        titulo="Evolución de la variación mensual del IPC",
        titulo_grafico="Variación intermensual del IPC",
        descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico=dict(Q4Etiquetas=True, etiquetaCadaSeis=True, precision=2)
    )
    subcap_data = datos.serie_historica("anual")
    reporte.agregar_subcapitulo(
        titulo="Evolución del cambio anual del IPC (Ritmo Inflacionario)",
        titulo_grafico="Variación interanual del IPC",
        descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico=dict(Q4Etiquetas=True, etiquetaCadaSeis=True, precision=2)
    )
# capitulos regionales
    region = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII'
    }
    for RegCod in range(1, 9):
        reporte.agregar_capitulo(
            titulo=f"Resultados para la región {region[RegCod]}"
        )
        subcap_data = datos.serie_IPC(RegCod)
        reporte.agregar_subcapitulo(
            titulo=f"Evolución del índice en la región {region[RegCod]}",
            titulo_grafico="Índice de la región, base diciembre del 2010",
            descripcion_grafico=f"Region {region[RegCod]}, serie histórica, adimensional",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="lineal",
            data=subcap_data[0],
            opciones_grafico={"precision":2, "Q4Etiquetas":True}
        )
        subcap_data = datos.serie_inflacion(RegCod, 'interanual', nivel=f'en la región {region[RegCod]}')
        reporte.agregar_subcapitulo(
            titulo=f"Evolución de la variación interanual del índice en la región {region[RegCod]}",
            titulo_grafico="Variación interanual del índice",
            descripcion_grafico=f"Region {region[RegCod]}, serie histórica, en porcentaje",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="lineal",
            data=subcap_data[0],
            opciones_grafico={"precision":2, "Q4Etiquetas":True}
        )
        subcap_data = datos.serie_inflacion(RegCod, 'acumulada', nivel=f'en la región {region[RegCod]}')
        reporte.agregar_subcapitulo(
            titulo=f"Evolución de la variación acumulada del índice en la región {region[RegCod]}",
            titulo_grafico="Variación acumulada del índice",
            descripcion_grafico=f"Region {region[RegCod]}, serie histórica, en porcentaje",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="columna",
            data=subcap_data[0],
            opciones_grafico={}
        )
        subcap_data = datos.serie_inflacion(RegCod, 'intermensual', nivel=f'en la región {region[RegCod]}')
        reporte.agregar_subcapitulo(
            titulo=f"Evolución de la variación mensual del índice en la región {region[RegCod]}",
            titulo_grafico="Variación intermensual del índice",
            descripcion_grafico=f"Region {region[RegCod]}, serie histórica, en porcentaje",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="lineal",
            data=subcap_data[0],
            opciones_grafico={"precision":2, "Q4Etiquetas":True}
        )
        subcap_data = datos.incidencias_divisiones(RegCod)
        reporte.agregar_subcapitulo(
            titulo="Incidencias mensuales por división de gasto básico",
            titulo_grafico="Incidencias mensuales",
            descripcion_grafico=f"Region {region[RegCod]}, {fecha}, en porcentaje",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="barra",
            data=subcap_data[0],
            opciones_grafico={"precision":2}
        )
        subcap_data = datos.incidencias_gba(RegCod, True)
        reporte.agregar_subcapitulo(
            titulo="Gastos básicos con mayor impacto positivo en la variación mensual",
            titulo_grafico="Gastos básicos con mayor incidencia positiva",
            descripcion_grafico=f"Region {region[RegCod]}, {fecha}, en porcentaje",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="barra",
            data=subcap_data[0],
            opciones_grafico={"precision":2}
        )
        subcap_data = datos.incidencias_gba(RegCod, False)
        reporte.agregar_subcapitulo(
            titulo="Gastos básicos con mayor impacto negativo en la variación mensual",
            titulo_grafico="Gastos básicos con mayor incidencia negativa",
            descripcion_grafico=f"Region {region[RegCod]}, {fecha}, en porcentaje",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="barra",
            data=subcap_data[0],
            opciones_grafico={"precision":2}
        )
        """
        subcap_data = datos.serie_poder_adquisitivo(RegCod)
        reporte.agregar_subcapitulo(
            titulo="Valor del Quetzal",
            titulo_grafico="Poder adquisitivo del quetzal",
            descripcion_grafico=f"Region {region[RegCod]}, serie histórica, adimensional",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="lineal",
            data=subcap_data[0],
            opciones_grafico={"precision":2, "Q4Etiquetas":True}
        )
        """
#capitulo 4
    reporte.agregar_capitulo(
        titulo="Anexos",
        anexo=True
    )
    datos_gba = datos.series_Gba(0)
    for Gba in datos_gba:
        nombre = Gba[0]
        datosGba = Gba[1]
        desc = Gba[2]
        reporte.agregar_subcapitulo(
            titulo=f"Evolución del índice del gasto básico {nombre}",
            titulo_grafico="IPC, base diciembre del 2010",
            descripcion_grafico="República de Guatemala, serie histórica, adimensional",
            descripcion=desc,
            fuente="INE",
            tipo_grafico="lineal",
            data=datosGba,
            opciones_grafico={"precision":2, "Q4Etiquetas":True}
        )
    print(f"Manipulacion de datos [{time()-t:.2f} s]")
    reporte.crear_reporte()
    print(f"Crear reporte [{(time()-t)//60:.2f} min]")
    reporte.compilar_reporte()
    reporte.compilar_reporte()
    tf = time()
    print(f"[{(tf-t)//60:.2f} min]")