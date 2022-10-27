from reporteine import ReporteINE
from time import time
from datosipc import datosIPC

if __name__ == "__main__":
    t = time()
    mes = 9
    anio = 2022
    datos = datosIPC(anio, mes)
    reporte = ReporteINE(
        nombre="Prueba_IPC"
    )
# capitulo 1
    introduccion = f"""El presente informe mensual, contiene los principales
                    resultados del Índice de Precios al Consumidor (IPC) del
                    Instituto Nacional de Estadística (INE). Como indicador
                    macroeconómico, este dato se utiliza para medir el comportamiento
                    del nivel general de precios de la economía del país, tomando
                    como base los precios observados en el mes de referencia.

                    Los niveles de inflación más importantes de septiembre de 2022
                    son los siguientes: se registró una inflación mensual de 0.36\%,
                    ritmo inflacionario de 9.03\% y una inflación acumulada de 7.93\%.

                    Este informe se compone de seis apartados y tres anexos: el
                    primero incluye el número índice y los resultados de las
                    inflaciones mensuales, acumuladas e interanuales a nivel
                    república, en el segundo se exponen las variaciones mensuales
                    históricas, por región y por división de gasto, en el tercero
                    se muestran los ritmos inflacionarios históricos, por región
                    y por división de gasto, en el cuarto se presentan las
                    principales alzas y bajas de los productos que conforman el
                    IPC y su incidencia en la inflación mensual; en el quinto se
                    describen las principales alzas y bajas de los productos que
                    conforman el IPC y su incidencia en el ritmo inflacionario;
                    en el sexto se consigna la evolución del poder adquisitivo del
                    quetzal; anexo 1: tablas de índices e inflaciones por región
                    y por división de gasto.

                    Finalmente, para mayor comprensión del documento, se incluye
                    un anexo 2 y 3 que contiene el glosario, con la definición de
                    los principales conceptos relacionados con el IPC y la metodología
                    de cálculo de las formulas más utilizadas para la obtención
                    de los diferentes índices y variaciones."""
    reporte.agregar_capitulo(
        titulo="Detalle del operativo de campo del IPC"
    )
    subcap_data = datos.serie_fuentes()
    reporte.agregar_subcapitulo(
        titulo="Cobertura de fuentes",
        titulo_grafico="Histórico de cobertura de fuentes, 1 año",
        descripcion_grafico="Cantidad de fuentes consultadas",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico=dict(Q4Etiquetas=True, inicio=2000, final = 9000)
    )
    subcap_data = datos.serie_precios(Qcobertura=True)
    reporte.agregar_subcapitulo(
        titulo="Cobertura de precios",
        titulo_grafico="Histórico de cobertura de precios, 1 año",
        descripcion_grafico="Cantidad de precios diligenciados",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico=dict(Q4Etiquetas=True)
    )
    subcap_data = datos.serie_precios(Qcobertura=False)
    reporte.agregar_subcapitulo(
        titulo="Imputación de precios",
        titulo_grafico="Histórico de imputación de precios, 1 año",
        descripcion_grafico="Cantidad de precios imputados",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico=dict(Q4Etiquetas=True)
    )
    subcap_data = datos.desagregacion_fuentes(mes)
    reporte.agregar_subcapitulo(
        titulo="Desagregación de fuentes",
        titulo_grafico="Desagregación porcentual de fuentes por tipo, 1 año",
        descripcion_grafico="Desagregación por tipo, porcentaje",
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
        opciones_grafico=dict(Q4Etiquetas=True)
    )
    
    subcap_data = datos.petroleo()
    reporte.agregar_subcapitulo(
        titulo="Precio del pretróleo",
        titulo_grafico="Precio promedio mensual del barril del petróleo",
        descripcion_grafico="Indicador internacional, serie histórica, en dólares por barril",
        descripcion=subcap_data[1],
        fuente="FRED",
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
        titulo="Índice de precios al consumidor de EE.UU.",
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
        titulo="Índice de precios al consumidor de México",
        titulo_grafico="Variación interanual del IPC de México",
        descripcion_grafico="Estados Unidos Mexicanos, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="FRED",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.inflacion()
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
# capitulo 3
    reporte.agregar_capitulo(
        titulo="Resultados del IPC"
    )
    subcap_data = datos.serie_IPC(0)
    reporte.agregar_subcapitulo(
        titulo="Evolución del IPC",
        titulo_grafico="IPC, base diciembre del 2010",
        descripcion_grafico="República de Guatemala, Serie histórica 1 año, adimensional",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.serie_inflacion(0, 'interanual')
    reporte.agregar_subcapitulo(
        titulo="Evolución del cambio anual del IPC",
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
        titulo="Evolución del cambio acumulado del IPC",
        titulo_grafico="Variación acumulada del IPC",
        descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.serie_inflacion(0, 'intermensual')
    reporte.agregar_subcapitulo(
        titulo="Evolución del cambio mensual del IPC",
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
        descripcion_grafico="República de Guatemala, Incidencias mensuales, porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="barra",
        data=subcap_data[0],
        opciones_grafico={"precision":2}
    )
    subcap_data = datos.serie_poder_adquisitivo(0)
    reporte.agregar_subcapitulo(
        titulo="Valor del dinero",
        titulo_grafico="Poder adquisitivo del quetzal",
        descripcion_grafico="República de Guatemala, serie histórica mensual, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
# capitulos regionales
    region = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'VI',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII'
    }
    for RegCod in range(1, 9):
        reporte.agregar_capitulo(
            titulo=f"Resultados del IPC para la region {region[RegCod]}"
        )
        subcap_data = datos.serie_IPC(RegCod)
        reporte.agregar_subcapitulo(
            titulo="Evolución del IPC",
            titulo_grafico="IPC, base diciembre del 2010",
            descripcion_grafico=f"Region {region[RegCod]}, Serie histórica 1 año, adimensional",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="lineal",
            data=subcap_data[0],
            opciones_grafico={"precision":2, "Q4Etiquetas":True}
        )
        subcap_data = datos.serie_inflacion(RegCod, 'interanual')
        reporte.agregar_subcapitulo(
            titulo="Evolución del cambio anual del IPC",
            titulo_grafico="Variación interanual del IPC",
            descripcion_grafico=f"Region {region[RegCod]}, serie histórica, en porcentaje",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="lineal",
            data=subcap_data[0],
            opciones_grafico={"precision":2, "Q4Etiquetas":True}
        )
        subcap_data = datos.serie_inflacion(RegCod, 'acumulada')
        reporte.agregar_subcapitulo(
            titulo="Evolución del cambio acumulado del IPC",
            titulo_grafico="Variación acumulada del IPC",
            descripcion_grafico=f"Region {region[RegCod]}, serie histórica, en porcentaje",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="lineal",
            data=subcap_data[0],
            opciones_grafico={"precision":2, "Q4Etiquetas":True}
        )
        subcap_data = datos.serie_inflacion(RegCod, 'intermensual')
        reporte.agregar_subcapitulo(
            titulo="Evolución del cambio mensual del IPC",
            titulo_grafico="Variación intermensual del IPC",
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
            descripcion_grafico=f"Region {region[RegCod]}, Incidencias mensuales, porcentaje",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="barra",
            data=subcap_data[0],
            opciones_grafico={"precision":2}
        )
        subcap_data = datos.serie_poder_adquisitivo(RegCod)
        reporte.agregar_subcapitulo(
            titulo="Valor del dinero",
            titulo_grafico="Poder adquisitivo del quetzal",
            descripcion_grafico=f"Region {region[RegCod]}, serie histórica mensual, en porcentaje",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="lineal",
            data=subcap_data[0],
            opciones_grafico={"precision":2, "Q4Etiquetas":True}
        )
#capitulo 4
    reporte.agregar_capitulo(
        titulo="Anexos"
    )
    datos_gba = datos.series_Gba(0)
    for Gba in datos_gba:
        nombre = Gba[0]
        datosGba = Gba[1]
        desc = Gba[2]
        reporte.agregar_subcapitulo(
            titulo=f"Evolución del IPC del gasto basico {nombre}",
            titulo_grafico="IPC, base diciembre del 2010",
            descripcion_grafico="República de Guatemala, Serie histórica 1 año, adimensional",
            descripcion=desc,
            fuente="INE",
            tipo_grafico="lineal",
            data=datosGba,
            opciones_grafico={"precision":2, "Q4Etiquetas":True}
        )
    print(f"Generacion de datos [{time()-t:.2f} s]")
    reporte.crear_reporte()
    #reporte.compilar_reporte()
    tf = time()
    print(f"[{(tf-t)//60:.2f} min]")