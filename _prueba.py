from datosipc import datosIPC
datos = datosIPC(2023, 3, dbBackup=1)
print(datos.series_Gba(0)[0])