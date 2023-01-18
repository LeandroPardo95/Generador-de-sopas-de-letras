import random
import numpy as np

def set_dimention(x,y):
    return np.zeros((x,y))

def set_word(word, position):
    pass

def set_position(words_list: list, matriz):
    for word in words_list:

        # Tener en cuenta que puede pasar que la palabra no entre, por lo tanto si o si tiene que ir en otra orientación.

        orientation = "vertical" if random.randint(0,1) == 0 else "horizontal"

        if orientation == "vertical":
            axisX = random.randint(0, int(np.shape(matriz)[1]) - 1)
            axisY = random.randint(0, int(np.shape(matriz)[0]) - len(word) - 1)

        
        else:
            axisY = random.randint(0, int(np.shape(matriz)[1]) - 1)
            axisX = random.randint(0, int(np.shape(matriz)[0]) - len(word) - 1)

        print(f"La palabra {word} va a tener una orientación {orientation} y va a comenzar ubicada en la posición: [{axisX},{axisY}].")
            







sopa_de_letras = set_dimention(50,10)
print(np.shape(sopa_de_letras)[0])

set_position(['hola','oso','gato'], sopa_de_letras)

sopa_de_letras[2,1] = 1