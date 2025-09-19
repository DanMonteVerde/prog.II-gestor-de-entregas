import json
#DEPOIS DE CRIAR OS METODOS DE PEGAR INFORMAÇÕES, FAZER ISSO PRA NAO TER ERRO DE ID, TENHO O EXEMPLLO NO CODIGO DA BIBLIOTECA VIRTUAL
def pegarid(classe):
    pass

#pegarinformacoes("entrega")
#pega as informacoes do json entrega
#e assim com os outros json
#Talvez seja necessario fazser uma checagem pra ver se existe, porem nao vou fazer agr
def pegarinformacoes(arquivo):
    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
    print(dados)
    return dados

di = {"id": "id", "conteudo": "conteudo"}
def mandarinformacoes(arquivo, adicionar):
    dados = pegarinformacoes(arquivo)
    #informações, tem que ver como vai mandar dados
    #nesse momento ele ta esperando adicionar como um dicionario com as chaves id e conteudo
    a = adicionar["id"]
    dados[str(a)] = adicionar["conteudo"]
    with open(f"{arquivo}.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)
    print(dados)
    return True
#PARA TESTES
if __name__ == "__main__":
    pegarinformacoes("motorista")
    pegarinformacoes("entrega")
    pegarinformacoes("veiculo")
    mandarinformacoes("motorista", di)