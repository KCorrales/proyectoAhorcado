import random

#lista con todos los estados del ahorcado. se seleccionara con el indice de intentos para mostrar en la interfaz.
Estado_ahorcado=[ 
      "-------\n |  |\n    |\n    |\n    |\n    |\n========= ",
      "-------\n |  |\n O  |\n    |\n    |\n    |\n========= ",
      "-------\n |  |\n O  |\n |  |\n    |\n    |\n========= ",
      "-------\n |  |\n O  |\n/|  |\n    |\n    |\n========= ",
      "-------\n |  |\n O  |\n/|\ |\n    |\n    |\n========= ",
      "-------\n |  |\n O  |\n/|\ |\n/   |\n    |\n========= ",
      "-------\n |  |\n O  |\n/|\ |\n/ \ |\n    |\n========= ",]

#punto 2 c funcion seleccionar palabra*****

def seleccionar_palabra(lista_palabras):
    total_palabras = len(lista_palabras)
    indice = random.randint(0, total_palabras - 1)  # aleatorio, pero siempre queda dentro de la lista
    return lista_palabras[indice]


# esta funcion es para preguntar al usuario una vez finalizada la partida si desea continuar o cerrar el juego. se realiza validacion solo acepta S o N 

def preguntar_continuar():
    while True:

        jugar=input("Desea volver a jugar? S/N\n").upper
        if jugar== "S":
            return True
        if jugar =="N":
            print("fin del juego")
            return False
        else: print("Ingrese S para seguir jugando o N para salir. \n")

#lo del dibujo
def mostrar_ahorcado(intentos_restantes):
    print(Estado_ahorcado[6 - intentos_restantes])

#se ingresa una letra y si es valida se actualiza el estado dependiendo de si está o no está.
def manejar_turno(palabra, estado, letras_adivinadas, intentos_restantes):
    letra = input("\nadivina una letra: ").upper()

    #evaluar si colocamos una regex para validar alfabeto.

    #validacion de cantidad de letras ingresadas por el usuario. 
    if len(letra) != 1 :
        print("solo puedes ingresar una sola letra a la vez, vuelve a intentarlo\n")
        return intentos_restantes
    
    #validación de no repeticion de letras por el usuario. 
    if letra in letras_adivinadas:
        print("ya se probó esa letra. Trata con otra.")
        return intentos_restantes
    
    #almacenamos la letra ingresada en una lista.
    letras_adivinadas.append(letra)

    #recorremos la palabra a adivinar para validar si la letra esta dentro de la palabra y de ser asi se cambia el estado del ahorcado en base al indice, si es incorrecto se resta uno de los intentos. 
    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                estado[i] = letra
        print("¡Correcto!\n")
    else:
        #se va descontando del total hasta llegar a 0
        intentos_restantes -= 1
        print("No está esa letra en la palabra")
    return intentos_restantes

def verificar_fin_del_juego(estado, intentos_restantes, palabra):
    #como ya no hay espacios, quiere decir que la palabra está completa
    if "_" not in estado:
        print("Felicidades, adivinaste que la palabra era", "".join(estado),"\n")
      
        
        jugar=preguntar_continuar()
        return jugar 

    if intentos_restantes == 0:
        #se le acabaron los intetos al jugador, entonces pierde
        print("Intentos restantes:", intentos_restantes)
        print(Estado_ahorcado[6])  #imprimir el muñeco ahorcado cuando se pierde    
        print("Perdiste, la palabra era", palabra,"\n")
        
        jugar=preguntar_continuar()
        return jugar 
      
    return None

#declaramos la funcion para dar inicio al juego al seleccionarse la opción a.
def iniciarJuego():
    #se declara una variable donde se guardaran los datos del return y se ejecuta la funcion cargar_palabras() como argumento a esta funcion enviamos el archivo palabras.txt que esta en la raiz de la carpeta del programa.
    lista_palabras=cargar_palabras("palabras.txt")


    #recibimos el nombre del jugador.
    player=input("\nIngrese su nombre: \n")

    print("¡Hola ",player," bienvenido/a al juego de ahorcado!\n")

    palabra = seleccionar_palabra(lista_palabras)
    estado = ["_" for _ in palabra]
    letras_adivinadas = []
    intentos_restantes = 6

    while True:
        
        print("Intentos restantes:", intentos_restantes)
        mostrar_ahorcado(intentos_restantes)
        print("\nPalabra a adivinar: ", " ".join(estado))
       
        intentos_restantes = manejar_turno(palabra, estado, letras_adivinadas, intentos_restantes)

        jugar=verificar_fin_del_juego(estado, intentos_restantes, palabra)


        if jugar is not None:
            return jugar

#punto 2 b*************************************************************************
#Se define la funcion cargar palabras

def cargar_palabras(archivo):


    #se declara la lista donde se almacenaran las palabras que existen en el archivo txt
    palabras=[]
    #se usa with open para abrir el archivo y asegurarse que se cerrara luego de usarse.
    #para abrir un documento existen diferentes formas de hacerlo, utilizaremos el modo r (solo lectura (read)) y lo llamaremos "archivo"
    with open(archivo, 'r') as archivo:
        #en este ciclo para cada palabra dentro del archivo vamos a hacer un append a la lista utilizando strip ya que las palabras del archivo estan separadas por saltos de linea. 
        for palabra in archivo:
            palabras.append(palabra.strip().upper())
    #return es el valor que nos retornara al finalizar la funcion, en este caso la lista "palabras[]"
    return palabras



#declaramos la funcion menu con el ciclo para el menu.
def menu():
    jugar=True

    while jugar:
        print("\nMenu principal")
        print("a: Jugar")
        print("b. Salir")
    #recibimos input con la opcion seleccionada por el usuario
        opcionMenu=input("\nSeleccione una de las opcciones del menu.\n")

    #utilizamos lower para validar la letra incluso si fue escrita en mayuscula
        if opcionMenu.lower() == "a":
            jugar=iniciarJuego()
            

        elif opcionMenu.lower() == "b":
            jugar=False
            return False
    # si el valor ingresado no es valido se reintentara devolviendo a la opcion de ingresar un nuevo input par ala opcionMenu.
        else:
            print("\nNo ha seleccionado una opción valida")

#llamamos a la funcion menu.
menu()
