# Prova exercicio 3
def Circulo(raio):
    
    areaCirculo = 3.14 * raio ** 2

    return areaCirculo

def Quadrado(lado):

    lado ** 2

    return areaQuadrado

def Retangulo(base, altura):

    base * altura

    return areaRetangulo

areaCirculo = Circulo()
areaQuadrado = Quadrado()
areaRetangulo = Retangulo()
lado = 0
base = 0
altura = 0
pi = float(3.14)



while(True):
    print("1. Circulo")
    print("2. Quadrado")
    print("3. Retangulo")

    escolha = int(input("Escolha o que deseja: "))

    if escolha == 1:
        raio = int(input("Quantos centimetros tem o raio: "))

        print("A area do circulo é: ")
        print(areaCirculo)
        print("Calculo encerrado.")
        break
    elif escolha == 2:
        lado = int(input("Quantos centimetros tem o lado: "))

        print("A area do quadrado é: ")
        print(areaQuadrado)
        print("Calculo encerrado.")
        break
    elif escolha == 3:
        base = int(input("Quantos centimetros tem a base: "))
        altura = int(input("Quantos centimetros tem a altura: "))

        print("A area do quadrado é: ")
        print(areaRetangulo)
        print("Calculo encerrado.")
        break
    else: 
        print("Escolha invalida")
        break

