from reporteine import ReporteINE
from time import time
from datosipc import datosIPC

if __name__ == "__main__":
    t = time()
    datos = datosIPC()
    reporte = ReporteINE(
        nombre="Prueba_IPC"
    )
    reporte.agregar_capitulo(
        titulo="Variables externas"
    )
    subcap_data = datos.indice_precio_alimentos()
    reporte.agregar_subcapitulo(
        indice_capitulo=0,
        titulo="Precio internacional de los alimentos",
        titulo_grafico="Índice de precios de los alimentos de la FAO",
        descripcion_grafico="Indicador internacional, serie histórica, adimensional",
        descripcion=subcap_data[1],
        fuente="FAO",
        tipo_grafico="lineal",
        data=subcap_data[0]
    )
    subcap_data = datos.petroleo()
    reporte.agregar_subcapitulo(
        indice_capitulo=0,
        titulo="Precio del pretróleo",
        titulo_grafico="Precio promedio mensual del barril del petróleo",
        descripcion_grafico="Indicador internacional, serie histórica, en dólares por barril",
        descripcion=subcap_data[1],
        fuente="FRED",
        tipo_grafico="lineal",
        data=subcap_data[0]
    )
    subcap_data = datos.cambio_quetzal()
    reporte.agregar_subcapitulo(
        indice_capitulo=0,
        titulo="Precio del pretróleo",
        titulo_grafico="Precio promedio mensual del barril del petróleo",
        descripcion_grafico="Indicador internacional, serie histórica, en dólares por barril",
        descripcion=subcap_data[1],
        fuente="FRED",
        tipo_grafico="lineal",
        data=subcap_data[0],
        precision=2
    )
    reporte.agregar_capitulo(
        titulo="Variables externas 2"
    )
    subcap_data = datos.ipc_mex()
    reporte.agregar_subcapitulo(
        indice_capitulo=1,
        titulo="Precio del pretróleo",
        titulo_grafico="Precio promedio mensual del barril del petróleo",
        descripcion_grafico="Indicador internacional, serie histórica, en dólares por barril",
        descripcion=subcap_data[1],
        fuente="FRED",
        tipo_grafico="lineal",
        data=subcap_data[0],
        precision=2
    )
    reporte.escribir_libros()
    reporte.generar_csv()
    reporte.hacer_graficas()
    reporte.hacer_descripciones()
    reporte.hacer_capitulos()
    reporte.crear_reporte()
    tf = time()
    print(f"{tf-t:.2f}")