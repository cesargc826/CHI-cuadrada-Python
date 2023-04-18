#Cesar Daniel Godinez Caudillo
#19630305  

def MetodoMultiplicativoCongruencias(i):
    a = int (input ("Ingresa el valor de a (recomendao: 73): "))
    n = int (input("Ingresa n1 (Debe ser numero primo)(recomendao: 11): "))
    m = int(input("Escribe el valor m (recomendao: 100): "))
    cont =0
    nums=[]
    for x in range(i):
        newVn=(a*n)%m
        print (newVn)
        n=newVn
        nums.append(newVn)
    return nums
