# Prova exercicio 4


matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input("Escolha um numero inteiro: "))
                   
for linha in matriz:
    print(linha)

print(f' Maior valor da diagonal principal {max(matriz = [i][j])}')
print(f' Menor valor de diagonal principal {min(matriz = [i][j])}')

