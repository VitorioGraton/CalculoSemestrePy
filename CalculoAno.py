# DEFINIÇÃO DOS SUBALGORITMOS
"""
Verifica se uma nota é valida
notaValida(nota: Float): Boolean
"""
def notaValida(nota):
    return nota >= 0 and nota <= 10
"""
Retorna mensagem de erro para nota inválida
msgNotaInvalida(nota: Float): void
"""
def msgNotaInvalida(nota):
    print(f"A nota {nota} é inválida. \nDigite uma nota entre 0 e 10: ", end='')
"""
Retorna o menor entre 3 numeros passados por parâmetro
menor3n(n1, n2, n3: Float): Float
"""
def menor3n(n1, n2, n3):
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor
"""
Calcula a média dos checkpoints
mediaCheckPoints(n1, n2, n3: Float): Float
"""
def mediaCheckPoints(n1, n2, n3):
    return (n1 + n2 + n3 - menor3n(n1,n2,n3)) / 2
"""
Calcula a média de dois numeros
media2n(n1, n2: Float): Float
"""
def media2n(n1, n2):
    return (n1 + n2) / 2
# ------------------------- PROGRAMA PRINCIPAL
# P R I M E I R O   S E M E S T R E
print(f"------------------------------- ")
print("PRIMEIRO SEMESTRE")
# Leitura dos checkpoints
chk1 = float(input("Digite o Checkpoint 1: "))
while not notaValida(chk1):
    msgNotaInvalida(chk1)
    chk1 = float(input())
chk2 = float(input("Digite o Checkpoint 2: "))
while not notaValida(chk2):
    msgNotaInvalida(chk2)
    chk2 = float(input())
chk3 = float(input("Digite o Checkpoint 3: "))
while not notaValida(chk3):
    msgNotaInvalida(chk3)
    chk3 = float(input())
# Calculando a média dos Checkpoints
mediaChk = mediaCheckPoints(chk1, chk2, chk3);
print(mediaChk)
# Leitura dos sprints
sprint1 = float(input("Digite o Sprint 1:"))
sprint2 = float(input("Digite o Sprint 2:"))
# Calcula a média dos sprints
mediaSprint = media2n(sprint1, sprint2)
# Leitura da prova semestral
semestral = float(input("Digite prova semestral:"))
while not notaValida(semestral):
    msgNotaInvalida(semestral)
    semestral =float(input())
# Ponderando os valores das médias
pontosChk = mediaChk * 0.2
pontosSprints = mediaSprint * 0.2
pontosSemestral = semestral * 0.6
# Cálculo da media do primeiro semestre
mediaPrimeiroSemestre = (pontosChk + pontosSprints + pontosSemestral)
# Pontos obtidos no primeiro semestre
pontosPrimeiroSemestre = mediaPrimeiroSemestre * 0.4
print(f"A sua média do primeiro semestre foi : {mediaPrimeiroSemestre}" )
if mediaPrimeiroSemestre <=5:
    print("Voce ficou de exame!")
elif mediaPrimeiroSemestre >= 6:
    print("Voce foi aprovado!")
else:
    print("Voce reprovou!")
# S E G U N D O   S E M E S T R E
print(f"------------------------------- ")
print("SEGUNDO SEMESTRE")
# Leitura dos checkpoints
chk1 = float(input("Digite o Checkpoint 1: "))
while not notaValida(chk1):
    msgNotaInvalida(chk1)
    chk1 = float(input())
chk2 = float(input("Digite o Checkpoint 2: "))
while not notaValida(chk2):
    msgNotaInvalida(chk2)
    chk2 = float(input())
chk3 = float(input("Digite o Checkpoint 3: "))
while not notaValida(chk3):
    msgNotaInvalida(chk3)
    chk3 = float(input())
# Calculando a média dos Checkpoints
mediaChk = mediaCheckPoints(chk1, chk2, chk3);
print(mediaChk)
# Leitura dos sprints
sprint1 = float(input("Digite o Sprint 1:"))
sprint2 = float(input("Digite o Sprint 2:"))
# Leitura da prova semestral
semestral = float(input("Digite prova semestral:"))
while not notaValida(semestral):
    msgNotaInvalida(semestral)
    semestral =float(input())
# Ponderando os valores das médias
pontosChk = mediaChk * 0.2
pontosSprints = mediaSprint * 0.2
pontosSemestral = semestral * 0.6
# Cálculo da media do primeiro semestre
mediaSegundoSemestre = (pontosChk + pontosSprints + pontosSemestral)
# Pontos obtidos no primeiro semestre
pontosSegundoSemestre = mediaSegundoSemestre * 0.6
print(f"A sua média do segundo semestre foi : {mediaSegundoSemestre}" )
if mediaPrimeiroSemestre <=5:
    print("Voce ficou de exame!")
if mediaPrimeiroSemestre >= 6:
    print("Voce está aprovdo para o proximo semestre!")
else:
    print("Voce reprovou e infelizmente nao esta no proximo semestre!")


"""




# Verificando o Checkpoint de menor valor
menor = chk1
if chk2 < menor:
    menor = chk2
if chk3 < menor:
    menor = chk3
# Calculando a média dos Checkpoints
mediaChk = (chk1 + chk2 + chk3 - menor) / 2
# Leitura dos Sprints
sprint1 = float(input("Digite o Sprint 1:"))
sprint2 = float(input("Digite o Sprint 2:"))
# Calculando a média dos Sprints
mediaSprint = (sprint1 + sprint2) / 2
# Leitura da prova semestral
semestral = float(input("Digite prova semestral:"))
# Ponderando os valores das médias
pontosChk = mediaChk * 0.2
pontosSprints = mediaSprint * 0.2
pontosSemestral = semestral * 0.6
# Cálculo da media do segundo semestre
mediaSegundoSemestre = (pontosChk + pontosSprints + pontosSemestral)
# Pontos obtidos no segundo semestre
pontosSegundoSemestre = mediaSegundoSemestre * 0.6
# Exibiçao da media do primeiro semetre
print(f"\nMédia do Primeiro Semestre: {mediaPrimeiroSemestre:.1f}")
# Exibiçao da media do segundo semetre
print(f"Média do Segundo Semestre: {mediaSegundoSemestre:.1f}")
# Cálculo da média final
mediaFinal = pontosPrimeiroSemestre + pontosSegundoSemestre
print(f"Média Final: {mediaFinal:.1f} - ", end="")
if mediaFinal >= 6:
    print("Aprovado!")
else:
    print("Não Aprovado!")
"""