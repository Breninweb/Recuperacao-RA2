# Prova exercicio 2

def listaPares():

    for num in range(10):
       if num % 2 == 0:
           pares.append(num)

    return pares



def listaImpares():

    for num in range(10):
       if num % 2 != 0:
           impares.append(num)

    return impares

pares = listaPares
impares = listaImpares
listaValores = []


for i in range(10):
    valoresInt = int(input("Digite um valor inteiro: "))
    listaValores.append(valoresInt)

for pares in range(i):
    print(pares % 2 == 0)

for impares in range(i):
    print(impares)