#print del muñeco del ahorcado.
print("-------\n |  |\n O  |\n/|\ |\n/ \ |\n    |\n========= ")

""" 
El programa va en funciones para mantener un poco mas el orden y trabajarlo un poco mas modular.  """

#declaramos la funcion para dar inicio al juego al seleccionarse la opción a.
def iniciarJuego(lista_palabras):
    #recibimos el nombre del jugador.
    player=input("\nIngrese su nombre: \n")

    print("!Hola ",player," bienvenido al juego de ahorcado!\n")
    seleccionar_palabra(lista_palabras)
    






#declaramos la funcion menu con el ciclo para el menu.
def menu(lista_palabras):
    while True:
        print("a: Jugar")
        print("b. Salir")
    #recibimos input con la opcion seleccionada por el usuario
        opcionMenu=input("\nSeleccione una de las opcciones del menu.\n")

    #utilizamos lower para validar la letra incluso si fue escrita en mayuscula
        if opcionMenu.lower() == "a":
            iniciarJuego(lista_palabras)

        elif opcionMenu.lower() == "b":
            break
    # si el valor ingresado no es valido se reintentara devolviendo a la opcion de ingresar un nuevo input par ala opcionMenu.
        else:
            print("\nNo ha seleccionado una opción valida")


#punto 2 b*************************************************************************
#Se define la funcion cargar palabras
def cargar_palabras(archivo):
    #se declara la lista donde se almacenaran las palabras que existen en el archivo.txt
    palabras=set()
    #Se utiliza with open para abrir el archivo y asegurarse que se cerrara luego de usarse.
    #para abrir un documento existen diferentes formas de hacerlo, utilizaremos el modo r (solo lectura (read)) y lo llamaremos "archivo"
    with open(archivo, 'r') as archivo:
        #en este ciclo para cada palabra dentro del archivo vamos a hacer un append a la lista utilizando strip ya que las palabras del archivo estan separadas por saltos de linea. 
        for palabra in archivo:
            palabras.add(palabra.strip())
    #return es el valor que nos retornara al finalizar la funcion, en este caso la lista "palabras[]"
    return palabras


#se declara una variable donde se guardaran los datos del return y se ejecuta la funcion cargar_palabras() como argumento a esta funcion enviamos el archivo palabras.txt que esta en la raiz de la carpeta del programa.
lista_palabras=cargar_palabras("palabras.txt")



#punto 2 c funcion seleccionar palabra*****
def seleccionar_palabra(lista_palabras):
    #aca estamos recibiendo el argumento que contiene toda la lista de palabras. 
    """ desarrollar el codigo de la funcion de seleccion aleatoria de palabras aqui. usaremos SET para simular que sea aleatorio. """
    #aca estoy probando imprimir el set de palabras. me quede pensando en como hacer para imprimir solo un elemento ya que es una lista no ordenada podria ser "aleatorio"
    for x in lista_palabras:
        print(x)
   



#este print es solo verificacion se requiere eliminar luego  *********************
print(lista_palabras)

#llamamos a la funcion menu.
menu(lista_palabras)
