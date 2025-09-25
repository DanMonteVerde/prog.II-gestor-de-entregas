import os
import time
import json
from utils import pegarinformacoes, salvarinformacoes, pegarid
from motoristas import Motorista
from veiculo import Veiculo
from entrega import Entrega
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def checararquivos():
    arquivos = ["motorista", "veiculo", "entrega"]

    for nome in arquivos:
        caminho = os.path.join(BASE_DIR, f"{nome}.json")
        if not os.path.exists(caminho):  # só cria se não existir
            salvarinformacoes(nome, {})
def saindo():
    for i in range(0, 3):
        print(".",end="", flush=True)
        time.sleep(0.4)
def menu():
    checararquivos()
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
            Motorista.cadastrar()
        elif opcao == "2":
            # if Veiculo.criar_veiculo() == False: 
            #     print("Cadastro cancelado", end = "")
            #     saindo()
            # else:
            #     input("Cadastro realizado com sucesso, pressione enter para continuar")

            Veiculo.cadastrar()
        elif opcao == "3":
            if Entrega.registrar_entrega() == True:
                input("BLA BLA")
            else:
                input("Pressione enter para continuar...")
                
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
    menu()