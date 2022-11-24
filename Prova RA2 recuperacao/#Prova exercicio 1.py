# Prova exercicio 1

listaAlunos = []

for aluno in range(5):
    nomeAluno = str(input("Qual o nome do aluno? "))
    listaAlunos.append(nomeAluno)


print(listaAlunos)


listaNotas = []

for nota in range(5):
    notas = float(input("Qual a nota? "))
    listaNotas.append(notas)

print(listaNotas)

aprovado = 7
recuperacao = float(7)
reprovado = float(4)

for i in range(5):
    if listaNotas[i] < reprovado:
        print(f'{listaAlunos[i]} esta reprovado com nota {listaNotas[i]}')        
    elif listaNotas[i] < recuperacao:
        print(f'{listaAlunos[i]} esta de recuperacao com nota {listaNotas[i]}')
    else:
        print(f'{listaAlunos[i]} esta aprovado com nota {listaNotas[i]}')