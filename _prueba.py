from reporteine import ReporteINE
from time import time
from datosipc import datosIPC
from funcionesjo import mes_by_ordinal

if __name__ == "__main__":
    t = time()
    mes = 1
    anio = 2022
    mes_ = mes_by_ordinal(mes, abreviado=False).capitalize()
    fecha = f"{mes_} {anio}"
    datos = datosIPC(anio, mes)
    print(f"Generacion de datos [{time()-t:.2f} s]")
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
    subcap_data = datos.serie_imputacion()
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
    print(f"Manipulacion de datos [{time()-t:.2f} s]")
    reporte.crear_reporte()
    #reporte.compilar_reporte()
    tf = time()
    print(f"[{(tf-t)//60:.2f} min]")