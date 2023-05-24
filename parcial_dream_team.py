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
    

def estadisticas_completas_jugador(lista_de_jugadores_original:list, indice:int) -> dict:
    """
    - Muestra las estadisticas completas de un jugador dado.
    - Recibe la lista de jugadores y un int que es un indice de la lista.
    - Retorna un dict.
    """
    lista_de_jugadores = lista_de_jugadores_original[:]

    return lista_de_jugadores[indice]["estadisticas"] 


def guardar_estadisticas_csv(lista_de_jugadores_original:list, indice:int):
    """
    - Guarda en un CSV las estadisticas del jugador seleccionado en el punto 2.
    - Recibe la lista de jugadores y el indice elegido anteriormente.
    - No retorna nada.
    """
    ruta = "C:\\Users\\Franco\\Desktop\\UTN FRA\\Tecnicatura Superior en Programacion\\1er Cuatrimestre\\Programacion I\\Ejercicios\\Archivos Stark\\"

    lista_de_jugadores = lista_de_jugadores_original[:]

    with open(ruta + lista_de_jugadores[indice]["nombre"], "w") as archivo:
        if type(contenido_a_guardar) == list:
            for elemento in contenido_a_guardar:         
                if len(llave) > 0:
                    mensaje = "{},{} \n".format(elemento["nombre"],
                                                elemento[llave])
                    archivo.write(mensaje)  
                else:
                    mensaje = "{} \n".format(elemento)
                    archivo.write(mensaje)  



def correr_programa():
    """
    - Se encarga de correr el programa principal
    - No recibe nada
    - No retorna nada
    """

    flag_segundo_punto = False

    while True:
        print("Menú de opciones:")
        print("1. Mostrar la lista de todos los jugadores del Dream Team")
        print("2. Ingresar un indice para ver estadisticas completas de ese jugador")
        print("3. ")
        print("4. ")
        print("5. ")
        print("6. ")
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

        while opcion < 0 and opcion > 23:
            opcion = int(input("\nOpcion invalida. Ingrese la opcion deseada\n"))

        if opcion == 1:
            mostrar_jugadores(lista_jugadores)

        elif opcion == 2:
            indice_elegido = input("Ingrese un indice para elegir un jugador de la lista y ver sus estadisticas (1 - 12)\n")
            coincidencia_indice = re.match(r"[0-9]{1,2}", indice_elegido)

            while not coincidencia_indice:
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

        elif opcion == 3 and flag_segundo_punto == True:
            


        elif opcion == 4:
            pass

        elif opcion == 5:
            pass

        elif opcion == 6:
            pass

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