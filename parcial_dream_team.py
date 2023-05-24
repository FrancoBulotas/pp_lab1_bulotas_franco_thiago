import json
import re

def leer_archivo(nombre_archivo:str):
    """
    - Abre en modo lectura el archivo dado
    - Recibe un string
    - Retorna la lista de heroes
    """
    lista = []
    ruta = "C:\\Users\\Franco\\Desktop\\UTN FRA\\Tecnicatura Superior en Programacion\\1er Cuatrimestre\\Laboratorio I\\Primer Parcial Repo\\"

    with open(ruta + nombre_archivo, "r") as archivo:
        # dict = json.load(archivo)
        # lista = dict["heroes"]
        return json.load(archivo)["jugadores"] 

    #return lista

lista_jugadores = leer_archivo("dream_team.json")

# 1
def mostrar_jugadores(lista_de_jugadores_original:list):
    """
    - Muestra la lista de jugadores del Dream Team
    - Recibe la lista de jugadores
    - No retorna nada
    """
    lista_de_jugadores = lista_de_jugadores_original[:]
    cont = 1

    for jugador in lista_de_jugadores:
        print("{} - {} - {}".format(cont, jugador["nombre"], jugador["posicion"]))
        cont += 1   
    
# 2
def estadisticas_completas_jugador(lista_de_jugadores_original:list, indice:int) -> dict:
    """
    - Muestra las estadisticas completas de un jugador dado.
    - Recibe la lista de jugadores y un int que es un indice de la lista.
    - Retorna un dict.
    """
    lista_de_jugadores = lista_de_jugadores_original[:]

    return lista_de_jugadores[indice]["estadisticas"] 

# 3
def guardar_estadisticas_csv(lista_de_jugadores_original:list, indice:int):
    """
    - Guarda en un CSV las estadisticas del jugador seleccionado en el punto 2.
    - Recibe la lista de jugadores y el indice elegido anteriormente.
    - No retorna nada.
    """
    ruta = "C:\\Users\\Franco\\Desktop\\UTN FRA\\Tecnicatura Superior en Programacion\\1er Cuatrimestre\\Laboratorio I\\Primer Parcial Repo\\Archivos Dream Team\\"

    lista_de_jugadores = lista_de_jugadores_original[:]

    with open(ruta + lista_de_jugadores[indice]["nombre"] + ".csv", "w") as archivo:
        for estadistica in lista_de_jugadores[indice]["estadisticas"]:         
            archivo.write("{},".format(estadistica))

        archivo.write("\n")  

        for estadistica in lista_de_jugadores[indice]["estadisticas"]: 
            archivo.write("{},".format(lista_de_jugadores[indice]["estadisticas"][estadistica]))  
            

# 4
def listar_logros_jugador(lista_de_jugadores_original:list, indice_jugador:int) -> list:
    """
    - Devuelve la lista de los logros de un jugador especificado por indice.
    - Recibe la lista de jugadores y un int con el indice de uno de ellos.
    - Retorna la lista de logros de dicho jugador.
    """
    lista_de_jugadores = lista_de_jugadores_original[:]

    return lista_de_jugadores[indice_jugador]["logros"]

def validacion_nombre(lista_de_jugadores_original:list, nombre_jugador:str) -> list:
    """
    - Valida si el nombre del jugador ingresado existe, si existe imprime sus logros.
    - Recibe el nombre del jugador ingresado y la lista de jugadores.
    - Retorna la lista de indices del/los jugadores elegidos.
    """
    lista_de_jugadores = lista_de_jugadores_original[:]

    lista_indice_nombres_elegidos = []
    for jugador in lista_de_jugadores:
        coincidencia_nombre_jugador = re.match("{}+".format(nombre_jugador.lower()), jugador["nombre"].lower())
        if coincidencia_nombre_jugador:
            lista_indice_nombres_elegidos.append(lista_de_jugadores.index(jugador))
    
    if len(lista_indice_nombres_elegidos) > 0:
        return lista_indice_nombres_elegidos
    else:
        nombre_jugador = input("Nombre inexistente. Ingrese el nombre del jugador cuyos logros quiere ver\n")
        validacion_nombre(lista_de_jugadores, nombre_jugador)


def imprimir_logros_jugador(lista_de_jugadores_original:list, lista_indice_nombres_elegidos:list, salon_de_la_fama:bool=False):
    """
    - Imprime los logros de los jugadores por nombre dado, o indica si estan en el salon de la fama
    - Recibe la lista de jugadores, la lista de indices de nombres elegidos y un bool indicando si se quiere saber si ingreso al salon de la fama o no.
    - No retorna nada
    """
    lista_de_jugadores = lista_de_jugadores_original[:]

    for indice_jugador in lista_indice_nombres_elegidos:
        lista_logros_del_jugador = listar_logros_jugador(lista_de_jugadores, indice_jugador)
        
        if salon_de_la_fama == False:
            print("Logros de {}:".format(lista_de_jugadores[indice_jugador]["nombre"]))

            for logro in lista_logros_del_jugador:
                print("{}".format(logro))
        else:
            if "Miembro del Salon de la Fama del Baloncesto" in lista_logros_del_jugador:
                print("{} es miembro del salon de la fama".format(lista_de_jugadores[indice_jugador]["nombre"]))


# 5
def promedio_equipo_por_llave(lista_de_jugadores_original:list, llave:str) -> int: 
    """
    - Se encarga de hallar el promedio del equipo de la llave dada.
    - Recibe una lista de jugadores y una llave del dict estadisticas.
    - Retorna el promedio (int)
    """
    lista_de_jugadores = lista_de_jugadores_original[:]
    acumulador = 0
    contador = 0

    for jugador in lista_de_jugadores:
        if type(jugador["estadisticas"][llave]) == type(int()) or type(jugador["estadisticas"][llave]) == type(float()):
            acumulador += jugador["estadisticas"][llave]
            contador += 1

    return acumulador / contador


def quicksort(lista_de_jugadores_original:list, flag_asc:bool, key:str)-> list:
    """
    - Se encarga de ordenar de manera ascendente o descendente los elementos dados. 
    - Recibe una lista de jugadores, una flag indicando si es asc o desc y una key del dict de la lista.
    - Retorna la lista ordenada.
    """
    lista_de_jugadores = lista_de_jugadores_original[:]
    mayores_pivot = []
    menores_pivot = []

    if len(lista_de_jugadores) <= 1:
        return lista_de_jugadores
    else:
        pivot = lista_de_jugadores[0]
        for jugador in lista_de_jugadores[1:]:
            if flag_asc == True:
                if jugador[key] > pivot[key]:
                    mayores_pivot.append(jugador)
                else:
                    menores_pivot.append(jugador)
            elif flag_asc == False:
                if jugador[key] < pivot[key]:
                    mayores_pivot.append(jugador)
                else:
                    menores_pivot.append(jugador)

    menores_pivot = quicksort(menores_pivot, flag_asc, key)
    menores_pivot.append(pivot)

    mayores_pivot = quicksort(mayores_pivot, flag_asc, key)
    menores_pivot.extend(mayores_pivot)

    return menores_pivot



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
        print("6. Ingresar nombre para ver si ese jugador es miembro del Salón de la Fama del Baloncesto")
        print("7. ")
        print("8. ")
        print("9. ")
        print("10. ")
        print("11. ")
        print("12. ")
        print("13. ")
        print("14. ")
        print("15. ")
        print("16. ")
        print("17. ")
        print("18. ")
        print("19. ")
        print("20. ")
        print("23. ")
        print("0. Salir del programa")
        
        opcion = int(input("\nIngrese la opcion deseada\n"))
        # CORREGIR ESTA VALIDACION
        while opcion < 0 or (opcion > 20 and opcion < 23) or opcion > 23 or opcion == "":
            opcion = int(input("\nOpcion invalida. Ingrese la opcion deseada\n"))

        if opcion == 1: 
            mostrar_jugadores(lista_jugadores)

        elif opcion == 2: # EMPROLIJAR ESTE ELIF (METER EN FUNCIONES DE SER POSIBLE)
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

        elif opcion == 3:
            if flag_segundo_punto == True:
                guardar_estadisticas_csv(lista_jugadores, indice_elegido)
            else:
                print("No podes guardar un archivo con las estadisticas de un jugador, ya que no elegiste uno. Debes pasar por el punto 2\n")

        elif opcion == 4:
            nombre_jugador = input("Ingrese el nombre del jugador cuyos logros quiere ver\n")

            lista_indice_nombres_elegidos_4 = validacion_nombre(lista_jugadores, nombre_jugador) #MIRAR FUNCION DE VALIDAR NOMBRE

            print(lista_indice_nombres_elegidos_4)

            imprimir_logros_jugador(lista_jugadores, lista_indice_nombres_elegidos_4)

        elif opcion == 5:
            print("El promedio de puntos por partido de todo el Dream Team junto es: {} puntos".format(promedio_equipo_por_llave(lista_jugadores, "promedio_puntos_por_partido")))
            print("Los jugadores ordenados alfabeticamente de forma ascendente, indicando su promedio puntos por partido")

            for jugador in quicksort(lista_jugadores, flag_asc=True, key="nombre"):
                print("- {} - {}".format(jugador["nombre"], jugador["estadisticas"]["promedio_puntos_por_partido"]))

        elif opcion == 6:
            nombre_jugador = input("Ingrese el nombre del jugador\n")

            lista_indice_nombres_elegidos_6 = validacion_nombre(lista_jugadores, nombre_jugador)

            imprimir_logros_jugador(lista_jugadores, lista_indice_nombres_elegidos_6, salon_de_la_fama=True)

        elif opcion == 7:
            pass

        elif opcion == 8:
            pass

        elif opcion == 9:
            pass

        elif opcion == 10:
            pass

        elif opcion == 11:
            pass

        elif opcion == 12:
            pass

        elif opcion == 13:
            pass

        elif opcion == 14:
            pass

        elif opcion == 15:
            pass

        elif opcion == 16:
            pass

        elif opcion == 17:
            pass

        elif opcion == 18:
            pass

        elif opcion == 19:
            pass

        elif opcion == 20:
            pass

        elif opcion == 23:
            pass

        elif opcion == 0:
            pass

        input("Presione enter para continuar\n")


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