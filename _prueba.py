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
    print(f"Carga de datos [{time()-t:.2f} s]")
    reporte = ReporteINE("Reporte febrero", anio, mes)
# capitulo 3
    reporte.agregar_capitulo(
        titulo="Resultados del IPC"
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
    reporte.crear_reporte()
    #reporte.compilar_reporte()
    tf = time()
    print(f"[{(tf-t)//60:.2f} min]")