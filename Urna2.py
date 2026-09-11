#Tem que fazer um contador para votos de cada candidato.
#Colocar os candidatos em uma lista e transformar em um objeto json.
#Fazer uma função que defina a porcentagem de voto e o vencedor da eleição.
import json
import os
os.system("cls")
candidatos = [
    #Políticos
    [1234, 5678,8901, 0000],
    #O número de votos
    [0,0,0,0],
    #Nome dos políticos
    ["Kazuma","Kratos","Salsicha","Branco"]
]
def resultado():
    total = 0
    for x in range(len(candidatos[0])):
        total += candidatos[1][x]
    print("Resultado da eleição:\n")
    for x in range(len(candidatos[0])):
        print(f"Candidato: {candidatos[2][x]} | {candidatos[0][x]}\n    Número de votos: {candidatos[1][x]} com {(candidatos[1][x]/total)*100:.2f}% dos votos\n")
    
while True:
    try:
        voto = int(input("Número do candidato: "))
        posicao = candidatos[0].index(voto)
        candidatos[1][posicao] +=1
    except ValueError:
        print("Digite um número seu(a) animal!")
    except KeyError:
        print("Candidato não encontrado, se quiser votar branco digite 0")
    except KeyboardInterrupt:
        os.system("cls")
        os.system("color 2")
        resultado()
        break