#Cesar Daniel Godinez Caudillo
#19630305   

def MetodoCongruencialAditivo (nums):
    # Método para generar números pseudoaleatorios mediante el método congruencial aditivo
    a = int(input("Ingrese el valor de a (recomendado: 7): "))
    c = int(input("Ingrese el valor de c (recomendado: 11): "))
    k = int(input("Ingrese el valor de k (recomendado: 3): "))
    m = int(input("Ingrese el valor de m (recomendado: 1000): "))
    seeds = [int(x) for x in input("Ingrese las semillas separadas por espacios (recomendado: 991 111 771 602): ").split()]
    n=len(seeds)
    numbers=[]+seeds
    
    for i in range(nums-n):
        newSeed= (seeds[n-1]*a + seeds[(n-1)-k]*c)%m
        print(newSeed)
        seeds.pop(0)
        seeds.append(newSeed)
        numbers.append(newSeed)
    return numbers
