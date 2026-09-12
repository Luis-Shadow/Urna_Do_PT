import os
os.system("cls")
candidatos = [
    #Id dos políticos
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
        global flag_vencedor
    print("Resultado da eleição:\n")
    for x in range(len(candidatos[0])):
        print(f"Candidato: {candidatos[2][x]} | {candidatos[0][x]}\n    Número de votos: {candidatos[1][x]} com {(candidatos[1][x]/total)*100:.2f}% dos votos\n")
    print("Vencedor: ", candidatos[2][flag_vencedor])
    
while True:
    try:
        voto = int(input("Número do candidato: "))
        posicao = candidatos[0].index(voto)
        candidatos[1][posicao] +=1
        flag_vencedor = 0
        flag_maior = 0
        for x in range(len(candidatos[1])):
            if candidatos[1][x] > flag_maior:
                flag_maior += 1
                flag_vencedor = candidatos[1].index(candidatos[1][x])
    except ValueError:
        print("Digite um número seu(a) animal!")
    except KeyError:
        print("Candidato não encontrado, se quiser votar branco digite 0")
    except KeyboardInterrupt:
        os.system("cls")
        os.system("color 2")
        resultado()
        break