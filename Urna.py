import json
import os
os.system("cls")
log = [43,54,657]
while True:
    dados2 = {
    }
    try:
        nome = input("Digite seu nome: ")
        dados2[nome] = int(input("Digite o número do seu candidato: "))
    except KeyboardInterrupt:
        with open("Data.json", "a") as FILE:
                json.dump(dados2,FILE)
        print("Obrigado por nos visitar.")
        break
    except ValueError:
        print("Digita certo seu(a) animal, aqui não tolera erros não.")