'''Codigo básico para crear el juego "El Ahorcado" que se trata de adivinar una palabra que es seleccionada
aleatoriamente usando la libreria random e ira descontando vidas o contando los aciertos que se tengan
parte de formaciones realizadas en mi proceso de aprendizaje de programación usando el lenguaje Python'''

from random import choice

palabras=["panadero","dinosaurio","televisor","computadora","radio","hidrogeno","oxigeno"]
letra_correctas=[]
letras_incorrectas=[]
intentos=6
aciertos=0
juego_terminado=False


# se define una funcion que me permita ingresar otra lista de palabras en caso de que quiera
#seleccionar una paabra de una nueva lista
def elegir_palabra(lista_palabras):
    palabra_elegida=choice(lista_palabras)
    #para que no se repitan palabras en la lista
    letras_unicas=len(set(palabra_elegida))
    return palabra_elegida, letras_unicas

def pedir_letra():
    letra_elegida=""
    es_valida=False
    abecedario="abcdefghijklmnopqrstuvwxyz"

    while not es_valida:
        letra_elegida=input("elige una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida)==1:
            es_valida=True
        else:
            print("No has elegido una letra correcta")
    return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta=[]
    for l in palabra_elegida:
        if l in letra_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append("-")
    print(" ".join(lista_oculta))

def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin=False
    if letra_elegida in palabra_oculta and letra_elegida not in letra_correctas:
        letra_correctas.append(letra_elegida)
        coincidencias +=1
    elif letra_elegida in palabra_oculta and letra_elegida in letra_correctas:
        print("Ya has usado esa letra. Intenta con una diferentea"
              "")
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -=1
    if vidas ==0:
        fin=perder()
    elif coincidencias== letras_unicas:
        fin=ganar(palabra_oculta)

    return vidas, fin, coincidencias

def perder():
    print("Te has quedado sin vidas")
    print("La palabra oculta era " + palabra)

    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felicidades, has encontrado la palabra!!!")

    return True

palabra , letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print(" \n" + " * " * 20 + "\n")
    mostrar_nuevo_tablero(palabra)
    print("\n")
    print("Letras incorrectas: "+ "-".join(letras_incorrectas))
    print(f" Vidas: {intentos}")
    letra=pedir_letra()

    intentos, terminado, aciertos= chequear_letra(letra,palabra,intentos,aciertos)

    juego_terminado = terminado