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
    datos = datosIPC(anio, mes, True)
    reporte = ReporteINE("Prueba_IPC", anio, mes)
# capitulo 1
    reporte.presentacion(datos.introduccion())
# capitulo 3
    reporte.agregar_capitulo(
        titulo="Resultados del IPC"
    )
    subcap_data = ([('Tomate', 0.29225663818344755), ('Papa', 0.21025646190618483), ('Maíz', 0.05735033044517484), ('Almuerzo consumido fuera del hogar', 0.04091200776815026), ('Pan', 0.03681416671646271)], 'Los cinco principales gastos básicos que registran la mayor incidencia positiva mensual se encuentran: Tomate (0.29%), Papa (0.21%), Maíz (0.06%), Almuerzo consumido fuera del hogar (0.04%) y Pan (0.04%).')
    reporte.agregar_subcapitulo(
        titulo="Bienes con mayor impacto en el cambio mensual",
        titulo_grafico="Gastos básicos con mayor incidencia positiva",
        descripcion_grafico=f"República de Guatemala, {fecha}, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="barra",
        data=subcap_data[0],
        opciones_grafico={"precision":2}
    )
    subcap_data = ([('Servicio de transporte aéreo', -0.26660090110546747), ('Cebolla', -0.16110746579025978), ('Ejotes', -0.04725647505228565), ('Culantro', -0.04264263639079777), ('Frijol', -0.018218850313713734)], 'Los cinco principales gastos básicos que registran la mayor incidencia negativa mensual se encuentran: Servicio de transporte aéreo (-0.27%), Cebolla (-0.16%), Ejotes (-0.05%), Culantro (-0.04%) y Frijol (-0.02%).')
    reporte.agregar_subcapitulo(
        titulo="Bienes con mayor impacto en el cambio mensual",
        titulo_grafico="Gastos básicos con mayor incidencia negativa",
        descripcion_grafico=f"República de Guatemala, {fecha}, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="barra",
        data=subcap_data[0],
        opciones_grafico={"precision":2}
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
    datos_nuevos = [
        (([('Pan', 0.10400178117048355), ('Tomate', 0.1037912722646311), ('Almuerzo consumido fuera del hogar', 0.10260808594854406), ('Frutas de estación', 0.038641622137404595), ('Plátano', 0.03165736146451794)], 'Los cinco principales gastos básicos que registran la mayor incidencia positiva mensual se encuentran: Pan (0.10%), Tomate (0.10%), Almuerzo consumido fuera del hogar (0.10%), Frutas de estación (0.04%) y Plátano (0.03%).'), ([('Servicio de transporte aéreo', -0.5839277692960135), ('Gasolina superior', -0.030106966355668636), ('Cebolla', -0.023669578739044413), ('Ejotes', -0.016791694232400345), ('Productos de tortillería', -0.011517189708792702)], 'Los cinco principales gastos básicos que registran la mayor incidencia negativa mensual se encuentran: Servicio de transporte aéreo (-0.58%), Gasolina superior (-0.03%), Cebolla (-0.02%), Ejotes (-0.02%) y Productos de tortillería (-0.01%).')),
        (([('Tomate', 1.3200857158994628), ('Maíz', 0.530751121152216), ('Productos de tortillería', 0.18809570177915963), ('Elote', 0.05583813127849275), ('Otras comidas consumidas  fuera del hogar', 0.03982100294509225)], 'Los cinco principales gastos básicos que registran la mayor incidencia positiva mensual se encuentran: Tomate (1.32%), Maíz (0.53%), Productos de tortillería (0.19%), Elote (0.06%) y Otras comidas consumidas fuera del hogar (0.04%).'), ([('Culantro', -0.23168857949731736), ('Güisquil', -0.21024370274740795), ('Cebolla', -0.14817115100657596), ('Servicio de transporte aéreo', -0.06737369266147575), ('Frijol', -0.06493028886109634)], 'Los cinco principales gastos básicos que registran la mayor incidencia negativa mensual se encuentran: Culantro (-0.23%), Güisquil (-0.21%), Cebolla (-0.15%), Servicio de transporte aéreo (-0.07%) y Frijol (-0.06%).')),
        (([('Maíz', 0.09651670343523479), ('Naranja', 0.07255128774030885), ('Carne de res', 0.06288362117869511), ('Tomate', 0.03590784809328701), ('Frijol', 0.03542468452568539)], 'Los cinco principales gastos básicos que registran la mayor incidencia positiva mensual se encuentran: Maíz (0.10%), Naranja (0.07%), Carne de res (0.06%), Tomate (0.04%) y Frijol (0.04%).'), ([('Servicio de transporte aéreo', -0.3362488471478095), ('Productos de tortillería', -0.08876992436180234), ('Culantro', -0.04640105767412542), ('Cebolla', -0.03207301607311694), ('Pepino', -0.011294929089190045)], 'Los cinco principales gastos básicos que registran la mayor incidencia negativa mensual se encuentran: Servicio de transporte aéreo (-0.34%), Productos de tortillería (-0.09%), Culantro (-0.05%), Cebolla (-0.03%) y Pepino (-0.01%).')),
        (([('Productos de tortillería', 0.3674093698140503), ('Tomate', 0.20145560274030883), ('Papa', 0.15613982553933878), ('Güisquil', 0.07539566486532566), ('Repollo', 0.04737215395089576)], 'Los cinco principales gastos básicos que registran la mayor incidencia positiva mensual se encuentran: Productos de tortillería (0.37%), Tomate (0.20%), Papa (0.16%), Güisquil (0.08%) y Repollo (0.05%).'), ([('Cebolla', -0.3400418748138377), ('Servicio de transporte aéreo', -0.3043303178588145), ('Ejotes', -0.155470259137909), ('Culantro', -0.10433366069528963), ('Aguacate', -0.07615365473809617)], 'Los cinco principales gastos básicos que registran la mayor incidencia negativa mensual se encuentran: Cebolla (-0.34%), Servicio de transporte aéreo (-0.30%), Ejotes (-0.16%), Culantro (-0.10%) y Aguacate (-0.08%).')),
        (([('Tomate', 0.12678629994810575), ('Cebolla', 0.037843607939802834), ('Chile pimiento', 0.03728887195121946), ('Carne de res', 0.027521898676699456), ('Frutas de estación', 0.025703523611831883)], 'Los cinco principales gastos básicos que registran la mayor incidencia positiva mensual se encuentran: Tomate (0.13%), Cebolla (0.04%), Chile pimiento (0.04%), Carne de res (0.03%) y Frutas de estación (0.03%).'), ([('Productos de tortillería', -0.07499743902439007), ('Servicio de transporte aéreo', -0.05850149455111571), ('Pan', -0.023370744680851114), ('Culantro', -0.02246995913336791), ('Güisquil', -0.020200505967825712)], 'Los cinco principales gastos básicos que registran la mayor incidencia negativa mensual se encuentran: Productos de tortillería (-0.07%), Servicio de transporte aéreo (-0.06%), Pan (-0.02%), Culantro (-0.02%) y Güisquil (-0.02%).')),
        (([('Tomate', 0.5184526037439456), ('Papa', 0.13530757952611594), ('Maíz', 0.05213984683859142), ('Almuerzo consumido fuera del hogar', 0.0452313260898021), ('Plátano', 0.023099525461447837)], 'Los cinco principales gastos básicos que registran la mayor incidencia positiva mensual se encuentran: Tomate (0.52%), Papa (0.14%), Maíz (0.05%), Almuerzo consumido fuera del hogar (0.05%) y Plátano (0.02%).'), ([('Cebolla', -0.10594956931535536), ('Servicio de bus extraurbano', -0.09106160492211049), ('Servicio de transporte aéreo', -0.08318691451760701), ('Ejotes', -0.04232657154077756), ('Güisquil', -0.014539598769472434)], 'Los cinco principales gastos básicos que registran la mayor incidencia negativa mensual se encuentran: Cebolla (-0.11%), Servicio de bus extraurbano (-0.09%), Servicio de transporte aéreo (-0.08%), Ejotes (-0.04%) y Güisquil (-0.01%).')),
        (([('Papa', 1.2521325006675574), ('Güisquil', 0.33785365732087225), ('Tomate', 0.24396387627948424), ('Naranja', 0.09749937872719179), ('Frutas de estación', 0.08800961593235436)], 'Los cinco principales gastos básicos que registran la mayor incidencia positiva mensual se encuentran: Papa (1.25%), Güisquil (0.34%), Tomate (0.24%), Naranja (0.10%) y Frutas de estación (0.09%).'), ([('Cebolla', -0.711277765910102), ('Ejotes', -0.11069124343569202), ('Otras legumbres y hortalizas', -0.08493111615487331), ('Productos de tortillería', -0.06525706942590102), ('Culantro', -0.04716846995994661)], 'Los cinco principales gastos básicos que registran la mayor incidencia negativa mensual se encuentran: Cebolla (-0.71%), Ejotes (-0.11%), Otras legumbres y hortalizas (-0.08%), Productos de tortillería (-0.07%) y Culantro (-0.05%).')),
        (([('Productos de tortillería', 0.13526096590909176), ('Frutas de estación', 0.052608500468603644), ('Pan', 0.0436312412136833), ('Güisquil', 0.02848210285848182), ('Otras legumbres y hortalizas', 0.021571555178069298)], 'Los cinco principales gastos básicos que registran la mayor incidencia positiva mensual se encuentran: Productos de tortillería (0.14%), Frutas de estación (0.05%), Pan (0.04%), Güisquil (0.03%) y Otras legumbres y hortalizas (0.02%).'), ([('Frijol', -0.320721473758201), ('Servicio de transporte aéreo', -0.1180749133083411), ('Cebolla', -0.04592698687910029), ('Culantro', -0.03153172680412361), ('Gasolina superior', -0.030045909090909102)], 'Los cinco principales gastos básicos que registran la mayor incidencia negativa mensual se encuentran: Frijol (-0.32%), Servicio de transporte aéreo (-0.12%), Cebolla (-0.05%), Culantro (-0.03%) y Gasolina superior (-0.03%).'))
    ]
    for RegCod in range(1, 9):
        reporte.agregar_capitulo(
            titulo=f"Resultados para la región {region[RegCod]}"
        )

        subcap_data = datos_nuevos[RegCod-1][0]
        reporte.agregar_subcapitulo(
            titulo="Bienes con mayor impacto en el cambio mensual",
            titulo_grafico="Gastos básicos con mayor incidencia positiva",
            descripcion_grafico=f"Region {region[RegCod]}, {fecha}, en porcentaje",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="barra",
            data=subcap_data[0],
            opciones_grafico={"precision":2}
        )
        subcap_data = datos_nuevos[RegCod-1][1]
        reporte.agregar_subcapitulo(
            titulo="Bienes con mayor impacto en el cambio mensual",
            titulo_grafico="Gastos básicos con mayor incidencia negativa",
            descripcion_grafico=f"Region {region[RegCod]}, {fecha}, en porcentaje",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="barra",
            data=subcap_data[0],
            opciones_grafico={"precision":2}
        )


    print(f"Generacion de datos [{time()-t:.2f} s]")
    reporte.crear_reporte()
    #reporte.compilar_reporte()
    tf = time()
    print(f"[{(tf-t)//60:.2f} min]")