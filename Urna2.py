#Tem que fazer um contador para votos de cada candidato.
#Colocar os candidatos em uma lista e transformar em um objeto json.
#Fazer uma função que defina a porcentagem de voto e o vencedor da eleição.
import json
import os
os.system("cls")
candidatos = {
    #Kratos
    "1234": 0,
    #Kazuma
    "5678": 0,
    #Branco
    "0": 0
}
def resultado():
    pass
f = open("Data.json", "a")
while True:
    try:
        candidatos[input('Voto: ')] += 1
    except ValueError:
        print("Digite um número seu(a) animal!")
    except KeyError:
        print("Candidato não encontrado, se quiser votar branco digite 0")
    except KeyboardInterrupt:
        pass
    f.close()