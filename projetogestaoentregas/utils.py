import json
import os
#DEPOIS DE CRIAR OS METODOS DE PEGAR INFORMAÇÕES, FAZER ISSO PRA NAO TER ERRO DE ID, TENHO O EXEMPLLO NO CODIGO DA BIBLIOTECA VIRTUAL
def pegarid(arquivo):
    dados = pegarinformacoes(arquivo)
    if not dados:
        return 0
    l = []
    for j,k in dados.items(): 
        l.append(int(j))
    return max(l)

#pegarinformacoes("entrega")
#pega as informacoes do json entrega
#e assim com os outros json
#Talvez seja necessario fazser uma checagem pra ver se existe, porem nao vou fazer agr
def pegarinformacoes(arquivo):
    if os.path.exists(f"{arquivo}.json"):
        with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return []

di = {"id": "2", "placa": "122231", "modelo": "modelo"}
def salvarinformacoes(arquivo, dados):
    # dados = pegarinformacoes(arquivo)
    # if conteudo["id"] in dados.keys():
    #     return False
    # a = conteudo["id"]
    # del conteudo["id"]
    # dados[a] = conteudo
    
    with open(f"{arquivo}.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)
    # print(dados)
    return True
#PARA TESTES
if __name__ == "__main__":
    print(salvarinformacoes("entrega",di))