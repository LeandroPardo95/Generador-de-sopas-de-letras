import random
import numpy as np
from export.export import ExportMatriz
from cfg import min,max

class SoapGenerator():
    def __init__(self, words:list, y=20, x=20):
        self.matriz = None
        self.words = words
        self.height = y
        self.width = x

    def create_soap(self):

        self.set_dimention()
        self.set_position()
        self.complete_letters()

    def set_dimention(self):
        if self.height > max or self.width > max:
            raise Exception(f"Error - Las dimensiones superan los limites establecidos. ({max}x{max})")
        elif self.height < min or self.width < min:
            raise Exception(f"Error - Las dimensiones son menores a los limites establecidos. ({min}x{min}")
        
        self.matriz =  np.empty((self.width,self.height), dtype=str)
    
    def set_position(self):
        
        for word in self.words:

            # Tener en cuenta que puede pasar que la palabra no entre, por lo tanto si o si tiene que ir en otra orientación.

            orientation = "vertical" if random.randint(0,1) == 0 else "horizontal"

            if orientation == "vertical":
                axisX = random.randint(0, int(np.shape(self.matriz)[1]) - 1)
                axisY = random.randint(0, int(np.shape(self.matriz)[0]) - len(word) - 1)

            
            else:
                axisY = random.randint(0, int(np.shape(self.matriz)[1]) - 1)
                axisX = random.randint(0, int(np.shape(self.matriz)[0]) - len(word) - 1)

            self.set_word(word.upper(), orientation, axisY, axisX)

    def set_word(self, word, orientation, axisY, axisX):

    # Aca hay que hacer una verificacion que todos los lugares donde van a ir las letras esten vacios o coincidan las letras, si no coincide, la palabra debe reubicarse.

        for letter in word:
            if orientation == "vertical":
                axisY = 1 + axisY
            else:
                axisX = 1 + axisX

            self.matriz[axisY,axisX] = letter

    def complete_letters(self):
        alphabet = "abcdefghijklmnñopqrstuvwxyz"
        for i in range(np.shape(self.matriz)[0]):
            for j in range(np.shape(self.matriz)[1]):

                if self.matriz[i,j] == "":
                    print(self.matriz[i,j])
                    self.matriz[i,j] = random.choice(alphabet)

    def export(self):
        if self.matriz is not None:
            return ExportMatriz(self)
        else:
            raise Exception("Para exportar la sopa de letras primero debe ejecutar el metodo create_soap()")

