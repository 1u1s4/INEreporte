from datosipc import datosIPC

from funcionesjo import mes_by_ordinal
from reporteine import ReporteINE

mes = 3
anio = 2023
mes_ = mes_by_ordinal(mes, abreviado=False).capitalize()
fecha = f"{mes_} {anio}"
datos = datosIPC(anio, mes, dbBackup=True)
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

reporte.crear_reporte()

reporte.compilar_reporte()
reporte.compilar_reporte()