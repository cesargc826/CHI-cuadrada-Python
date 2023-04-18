#Cesar Daniel Godinez Caudillo
#19630305 

import random

def MiddleSquares(numbers):
    # Método para generar números pseudoaleatorios mediante el método de cuadrados medios
    seed = random.randint(1000,9999)
    print ("La semilla que se genero es la siguiente: ",seed)
    seedAux = seed #aux
    result = []
    for x in range(numbers):
        seedAux = seedAux * seedAux
        NumString = str(seedAux)
        digits = len(NumString)
        if digits < 8:
            NumString = ("0" * (8 - digits)) + NumString
        middle = NumString[2:6]
        print(middle)
        result.append(round(float(middle) / 10000, 4))
        seedAux = int(middle)
    return result

#numeros = MiddleSquares(10)
#print(numeros)
