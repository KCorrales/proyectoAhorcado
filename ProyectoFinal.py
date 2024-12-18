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

#lo del dibujo
def mostrar_ahorcado(intentos_restantes):
    print(Estado_ahorcado[6 - intentos_restantes])

#se ingresa una letra y si es valida se actualiza el estado dependiendo de si está o no está.
def manejar_turno(palabra, estado, letras_adivinadas, intentos_restantes):
    letra = input("\nadivina una letra: ").upper()
    if len(letra) != 1 or not letra.isalpha():
        print("solo puedes ingresar una sola letra a la vez")
        return intentos_restantes
    if letra in letras_adivinadas:
        print("ya se probó esa letra. Trata con otra.")
        return intentos_restantes
    letras_adivinadas.append(letra)
    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                estado[i] = letra
        print("correcto")
    else:
        #se va descontando del total hasta llegar a 0
        intentos_restantes -= 1
        print("no está esa letra")
    return intentos_restantes

def verificar_fin_del_juego(estado, intentos_restantes, palabra):
    #como ya no hay espacios, quiere decir que la palabra está completa
    if "_" not in estado:
        print("felicidades, adivinaste que la palabra era", "".join(estado))
        return True
    if intentos_restantes == 0:
        #se le acabaron los intetos al jugador, entonces pierde
        print("Intentos restantes:", intentos_restantes)
        print(Estado_ahorcado[6])  #imprimir el muñeco ahorcado cuando se pierde    
        print("perdiste, la palabra era", palabra,"\n")
        return True
    return False

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
        print("\nEstado actual: ", " ".join(estado))
        mostrar_ahorcado(intentos_restantes)
        print("Intentos restantes:", intentos_restantes)
        intentos_restantes = manejar_turno(palabra, estado, letras_adivinadas, intentos_restantes)
        if verificar_fin_del_juego(estado, intentos_restantes, palabra):
            break

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
    while True:
        print("a: Jugar")
        print("b. Salir")
    #recibimos input con la opcion seleccionada por el usuario
        opcionMenu=input("\nSeleccione una de las opcciones del menu.\n")

    #utilizamos lower para validar la letra incluso si fue escrita en mayuscula
        if opcionMenu.lower() == "a":
            iniciarJuego()

        elif opcionMenu.lower() == "b":
            break
    # si el valor ingresado no es valido se reintentara devolviendo a la opcion de ingresar un nuevo input par ala opcionMenu.
        else:
            print("\nNo ha seleccionado una opción valida")

#llamamos a la funcion menu.
menu()
