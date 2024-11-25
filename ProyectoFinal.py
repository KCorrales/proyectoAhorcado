#comentarios # son explicaciones, comentarios """  """ son ideas o pasos por realizar. 

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
#aca estamos recibiendo el argumento que contiene toda la lista de palabras. 
def seleccionar_palabra(lista_palabras):

    """ Esto es solo para prueba, lo que se requiere es variar el indice la la lista de palabras para asi siempre retornar una palabra diferente o buscar alguna forma de hacer un return aleatorio. """
    print(lista_palabras[0])
    palabra= lista_palabras[0]
    return palabra


#declaramos la funcion para dar inicio al juego al seleccionarse la opción a.
def iniciarJuego():
    
    #se declara una variable donde se guardaran los datos del return y se ejecuta la funcion cargar_palabras() como argumento a esta funcion enviamos el archivo palabras.txt que esta en la raiz de la carpeta del programa.
    lista_palabras=cargar_palabras("palabras.txt")

    #recibimos el nombre del jugador.
    player=input("\nIngrese su nombre: \n")

    print("!Hola ",player," bienvenido al juego de ahorcado!\n")

    seleccionar_palabra(lista_palabras)
    print("\n")


#punto 2 b*************************************************************************
#Se define la funcion cargar palabras
def cargar_palabras(archivo):
    #se declara la lista donde se almacenaran las palabras que existen en el archivo.txt
    palabras=[]
    #Se utiliza with open para abrir el archivo y asegurarse que se cerrara luego de usarse.
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
