from funciones_dream_team import *
import re


def correr_programa():
    """
    - Se encarga de correr el programa principal
    - No recibe nada
    - No retorna nada
    """
    flag_segundo_punto = False

    while True:
        print("Menú de opciones:")
        print("1. Mostrar la lista de todos los jugadores del Dream Team.")
        print("2. Ingresar un indice para ver estadisticas completas de ese jugador.")
        print("3. Guardar archivo con estadistias completas del jugador elegido en el punto 2.")
        print("4. Buscar un jugador por nombre para ver sus logros.")
        print("5. Ver el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.")
        print("6. Ingresar nombre para ver si ese jugador es miembro del Salón de la Fama del Baloncesto.")
        print("7. Ver el jugador con la mayor cantidad de rebotes totales.")
        print("8. Ver el jugador con el mayor porcentaje de tiros de campo.")
        print("9. Ver el jugador con la mayor cantidad de asistencias totales.")
        print("10. Ingresar un valor y ver los jugadores que han promediado más puntos por partido que ese valor.")
        print("11. Ingresar un valor y ver los jugadores que han promediado más rebotes por partido que ese valor.")
        print("12. Ingresar un valor y ver los jugadores que han promediado más asistencias por partido que ese valor.")
        print("13. Ver el jugador con la mayor cantidad de robos totales.")
        print("14. Ver el jugador con la mayor cantidad de bloqueos totales.")
        print("15. Ingresar un valor y ver los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.")
        print("16. Ver el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.")
        print("17. Ver el jugador con la mayor cantidad de logros obtenidos.")
        print("18. Ingresar un valor y ver los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.")
        print("19. Ver cual es el jugador con la mayor cantidad de temporadas jugadas.")
        print("20. Ingresar un valor y ver los jugadores, ordenados por posición en la cancha, que tengan un porcentaje de tiros de campo superior a ese valor.")
        print("23. Ver cuál es la posición de cada jugador en cada uno de los siguientes ranking (Puntos / Rebotes / Asistencias / Robos) y guardar en archivo.")
        print("0. Salir del programa")
        
        
        opcion = input("\nIngrese la opcion deseada\n")
    
        while validacion_menu(opcion) == False:
            opcion = input("Opcion invalida. Ingrese la opcion deseada\n")

        if opcion == "1": 
            mostrar_jugadores(lista_jugadores)

        elif opcion == "2": # EMPROLIJAR ESTE ELIF (METER EN FUNCIONES DE SER POSIBLE)
            indice_elegido = input("Ingrese un indice para elegir un jugador de la lista y ver sus estadisticas (1 - 12)\n")
            coincidencia_indice = re.match(r"[0-9]{1,2}", indice_elegido)

            while coincidencia_indice == None:
                indice_elegido = input("Indice invalido. Ingrese un indice para elegir un jugador de la lista y ver sus estadisticas (1 - 12)\n")
                coincidencia_indice = re.match(r"[0-9]{1,2}", indice_elegido)
                
            indice_elegido = int(indice_elegido)
            while indice_elegido < 1 or indice_elegido > 12:
                indice_elegido = input("Indice invalido. Ingrese un indice para elegir un jugador de la lista y ver sus estadisticas (1 - 12)\n")

            indice_elegido -= 1

            estadistica_jugador = estadisticas_completas_jugador(lista_jugadores, indice_elegido)

            print(lista_jugadores[indice_elegido]["nombre"])
            for estadistica in estadistica_jugador:
                print("{}: {}".format(estadistica, estadistica_jugador[estadistica]))

            flag_segundo_punto = True

        elif opcion == "3":
            if flag_segundo_punto == True:
                guardar_estadisticas_csv(lista_jugadores, indice_elegido)
                print("Archivo guardado!!")
            else:
                print("No podes guardar un archivo con las estadisticas de un jugador, ya que no elegiste uno. Debes pasar por el punto 2")

        elif opcion == "4":
            nombre_jugador = input("Ingrese el nombre del jugador cuyos logros quiere ver\n")

            lista_indice_nombres_elegidos_4 = validacion_nombre(lista_jugadores, nombre_jugador) # MIRAR FUNCION DE VALIDAR NOMBRE

            print(lista_indice_nombres_elegidos_4)

            imprimir_logros_jugador(lista_jugadores, lista_indice_nombres_elegidos_4)

        elif opcion == "5":
            print("El promedio de puntos por partido de todo el Dream Team junto es: {} puntos".format(promedio_equipo_por_llave(lista_jugadores, "promedio_puntos_por_partido")))
            print("Los jugadores ordenados alfabeticamente de forma ascendente, indicando su promedio puntos por partido")

            for jugador in quicksort(lista_jugadores, flag_asc=True, key="nombre"):
                print("- {} - {}".format(jugador["nombre"], jugador["estadisticas"]["promedio_puntos_por_partido"]))

        elif opcion == "6":
            nombre_jugador = input("Ingrese el nombre del jugador\n")

            lista_indice_nombres_elegidos_6 = (lista_jugadores, nombre_jugador)

            imprimir_logros_jugador(lista_jugadores, lista_indice_nombres_elegidos_6, salon_de_la_fama=True)

        elif opcion == "7":
            print("El jugador con mayor cantidad de rebotes es {} rebotes".format(calcular_max(lista_jugadores, llave="rebotes_totales")))

        elif opcion == 8:
            print("El jugador con mayor porcentaje de tiros de campo es {} %".format(calcular_max(lista_jugadores, llave="porcentaje_tiros_de_campo")))

        elif opcion == "9":
            print("El jugador con la mayor cantidad de asistencias totales es {} asistencias".format(calcular_max(lista_jugadores, llave="asistencias_totales")))

        elif opcion == "10":
            valor_ingresado_10 = input("Ingrese un valor\n")
        
            valor_ingresado_10 = validar_valor_ingresado(valor_ingresado_10) # TEMPORAL HASTA QUE VEA COMO SOLUCIONAR RECURSIVIDAD DE LA FUNCION VALIDAR_NOMBRE

            lista_indices_mayores_ppp = mayor_al_valor_ingresado(lista_jugadores, llave="promedio_puntos_por_partido", valor_ingresado=valor_ingresado_10)
            
            imprimir_nombre_jugador_por_indice(lista_jugadores, lista_indices_mayores_ppp, "puntos por partido")

        elif opcion == "11":
            valor_ingresado_11 = input("Ingrese un valor\n")
        
            valor_ingresado_11 = validar_valor_ingresado(valor_ingresado_11) # TEMPORAL HASTA QUE VEA COMO SOLUCIONAR RECURSIVIDAD DE LA FUNCION VALIDAR_NOMBRE

            lista_indices_mayores_rpp = mayor_al_valor_ingresado(lista_jugadores, llave="promedio_rebotes_por_partido", valor_ingresado=valor_ingresado_11)
            
            imprimir_nombre_jugador_por_indice(lista_jugadores, lista_indices_mayores_rpp, "rebotes por partido")

        elif opcion == "12":
            valor_ingresado_12 = input("Ingrese un valor\n")
        
            valor_ingresado_12 = validar_valor_ingresado(valor_ingresado_12) # TEMPORAL HASTA QUE VEA COMO SOLUCIONAR RECURSIVIDAD DE LA FUNCION VALIDAR_NOMBRE

            lista_indices_mayores_app = mayor_al_valor_ingresado(lista_jugadores, llave="promedio_asistencias_por_partido", valor_ingresado=valor_ingresado_12)
            
            imprimir_nombre_jugador_por_indice(lista_jugadores, lista_indices_mayores_app, "asistencias por partido")

        elif opcion == "13":
            print("El jugador con mayor cantidad de robos totales es {} robos".format(calcular_max(lista_jugadores, llave="robos_totales")))

        elif opcion == "14":
            print("El jugador con mayor cantidad de bloqueos totales es {} bloqueos".format(calcular_max(lista_jugadores, llave="bloqueos_totales")))

        elif opcion == "15":
            valor_ingresado_15 = input("Ingrese un valor\n")
        
            valor_ingresado_15 = validar_valor_ingresado(valor_ingresado_15) # TEMPORAL HASTA QUE VEA COMO SOLUCIONAR RECURSIVIDAD DE LA FUNCION VALIDAR_NOMBRE

            lista_indices_mayores_ptl = mayor_al_valor_ingresado(lista_jugadores, llave="porcentaje_tiros_libres", valor_ingresado=valor_ingresado_15)
            
            imprimir_nombre_jugador_por_indice(lista_jugadores, lista_indices_mayores_ptl, "porcentaje de tiros libres")

        elif opcion == "16":
            print("El promedio de puntos por partido de todo el Dream Team excluyendo al jugador con la menor cantidad de puntos por partido es de {} puntos"
                  .format(promedio_equipo_por_llave(lista_jugadores, "promedio_puntos_por_partido", excluir_menor=True)))

        elif opcion == "17":
            dict_jugador = jugador_mas_logros(lista_jugadores)

            print("El jugador con mas logros es {}, con los siguientes:".format(dict_jugador["nombre"]))
            for logro in dict_jugador["logros"]:
                print(logro)

        elif opcion == "18":
            valor_ingresado_18 = input("Ingrese un valor\n")
        
            valor_ingresado_18 = validar_valor_ingresado(valor_ingresado_18) # TEMPORAL HASTA QUE VEA COMO SOLUCIONAR RECURSIVIDAD DE LA FUNCION VALIDAR_NOMBRE

            lista_indices_mayores_ptt = mayor_al_valor_ingresado(lista_jugadores, llave="porcentaje_tiros_triples", valor_ingresado=valor_ingresado_18)
            
            imprimir_nombre_jugador_por_indice(lista_jugadores, lista_indices_mayores_ptt, "porcentaje de tiros triples")

        elif opcion == "19":
            print("El jugador con mayor cantidad de temporadas jugadas es {} temporadas".format(calcular_max(lista_jugadores, llave="temporadas")))

        elif opcion == "20":
            valor_ingresado_20 = input("Ingrese un valor\n")
        
            valor_ingresado_20 = validar_valor_ingresado(valor_ingresado_20) # TEMPORAL HASTA QUE VEA COMO SOLUCIONAR RECURSIVIDAD DE LA FUNCION VALIDAR_NOMBRE

            lista_indices_mayores_ptc = mayor_al_valor_ingresado(lista_jugadores, llave="porcentaje_tiros_de_campo", valor_ingresado=valor_ingresado_20)
            
            imprimir_nombre_jugador_por_indice(lista_jugadores, lista_indices_mayores_ptc, "porcentaje de tiros de campo", flag_posicion=True)

        elif opcion == "23":
            guardar_ranking_en_csv(lista_jugadores)

            print("Archivo guardado!!")

        elif opcion == "0":
            break

        input("\nPresione enter para continuar\n")


correr_programa()




# def validacion_nombre_e_imprime_logros(nombre_jugador:str) -> list:
#     """
#     - Valida si el nombre del jugador ingresado existe, si existe imprime sus logros
#     - Recibe el nombre del jugador ingresado
#     - No retorna nada
#     """
#     lista_indice_nombres_elegidos = []
#     for jugador in lista_jugadores:
#         coincidencia_nombre_jugador = re.match("{}+".format(nombre_jugador.lower()), jugador["nombre"].lower())
#         if coincidencia_nombre_jugador:
#             lista_indice_nombres_elegidos.append(lista_jugadores.index(jugador))
    
#     if len(lista_indice_nombres_elegidos) > 0:
#         for indice_jugador in lista_indice_nombres_elegidos:
#             lista_logros_del_jugador = listar_logros_jugador(lista_jugadores, indice_jugador)
#             print("Logros de {}:".format(lista_jugadores[indice_jugador]["nombre"]))
#             for logro in lista_logros_del_jugador:
#                 print("{}".format(logro))
#     else:
#         nombre_jugador = input("Nombre inexistente. Ingrese el nombre del jugador cuyos logros quiere ver\n")
#         validacion_nombre_e_imprime_logros(nombre_jugador)


# validacion_nombre_e_imprime_logros("mifasd")