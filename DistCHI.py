import scipy.stats as stats
import congruadi
import multiCongru
import cuadMed

nums=[]
n = 100 
opc = int (input ("1: Cuadrados medios \n2: Metodo congruencial aditivo \n3: Metodo multiplicativo de congruencias "))
if opc == 1:
    nums=cuadMed.MiddleSquares(n)
    for x in range(n):
        nums[x]=nums[x]/10000
elif opc ==2:
    nums=congruadi.MetodoCongruencialAditivo(n)
    for x in range(n):
        nums[x]=nums[x]/1000
elif opc ==3:
    nums=multiCongru.MetodoMultiplicativoCongruencias(n)
    for x in range(n):
        nums[x]=nums[x]/100
else:
    print ("Error")

m=n/10
c=1/m
valorCritico = stats.chi2.ppf(1 - 0.05, m-1)
Ei=n/m
Sumatoria=0
i=0
mn=0.0
mx=mn+c
for y in range(10):
    for x in range(n):
        if nums[x] >= mn and nums[x] <mx:
            i=+1
    Sumatoria=Sumatoria+(((Ei-i)*(Ei-i))/Ei)
    i=0
    mn=+c
    mx=+c

if Sumatoria < valorCritico:
    print("Uniforme")
else: 
    print("No uniforme")
