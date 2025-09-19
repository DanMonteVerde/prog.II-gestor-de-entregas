import os
import time
import json
from utils import pegarinformacoes
def saindo():
    for i in range(0, 3):
        print(".",end="", flush=True)
        time.sleep(0.4)
def menu():
    
    while True:
        #limpar o terminal
        os.system("cls")
        print("""1. Cadastrar motorista
2. Cadastrar veículo
3. Registrar entrega
4. Atualizar status da entrega
5. Listar entregas pendentes
6. Listar todas as entregas
0. Sair""")
        #pega a opção como string e tira os espaços
        opcao = input().lstrip()

        if opcao == "1":
            print("Cadastrar motorista")
        elif opcao == "2":
            print("Cadastrar veículo")
        elif opcao == "3":
            print("Registrar entrega")
        elif opcao == "4":
            print("Atualizar status da entrega")
        elif opcao == "5":
            print("Listar entregas pendentes")
        elif opcao == "6":
            print("Listar todas as entregas")
        
        elif opcao == "0":
            print("Saindo do programa",end = "")
            saindo()
            break
        else:
            input("Opção inválida. Pressione enter para continuar")

if __name__ == "__main__":
    pegarinformacoes("motorista")
    pegarinformacoes("entrega")
    pegarinformacoes("veiculo")
    
    #menu()