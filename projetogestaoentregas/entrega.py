from utils import pegarid, pegarinformacoes, salvarinformacoes
from motoristas import Motorista
from veiculo import Veiculo
def listarentregas(filtro=None):
    dados = pegarinformacoes("entrega")
    if not dados:
        return False
    else:
        if filtro == None:
            for k,i in dados.items():
                print(f"ID:{k}\nDescricao: {i['descricao']}\nStatus: {i['status']}")
                print()
                if i["motorista"]:
                    for j,m in i["motorista"].items():
                        print(f"ID Motorista: {j}\nNome: {m['nome']}\nCNH: {m['cnh']}")
                        print()
                if i["veiculo"]:
                    for j,v in i["veiculo"].items():
                        print(f"ID Veiculo: {j}\nPlaca: {v['placa']}\nModelo: {v['modelo']}")
                        print()
        else:
            cont=0
            for k,i in dados.items():
                if i["status"].lower() == filtro.lower():
                    cont+=1
                    print(f"ID:{k}\nDescricao: {i['descricao']}\nStatus: {i['status']}")
                    print()
                    if i["motorista"]:
                        for j,m in i["motorista"].items():
                            print(f"ID Motorista: {j}\nNome: {m['nome']}\nCNH: {m['cnh']}")
                            print()
                    if i["veiculo"]:
                        for j,v in i["veiculo"].items():
                            print(f"ID Veiculo: {j}\nPlaca: {v['placa']}\nModelo: {v['modelo']}")
                            print()
            if cont == 0:
                print("Sem entregas com esse filtro")

def atualizar_status():
    listarentregas()
    input(pegarinformacoes("entrega").keys())
    if pegarinformacoes("entrega") == {}:
        print("Sem entregas cadastradas")
        return False
    id = input("Digite o ID da entrega: ")  
    if id not in pegarinformacoes("entrega").keys():
        print("ID nao encontrado")
        return False
    
    status = input("Digite o novo status da entrega: ")
    dados = pegarinformacoes("entrega")
    dados[id]["status"] = status
    
    salvarinformacoes("entrega", dados)
    print("Status da entrega atualizado com sucesso")
class Entrega():
    idcont = 1
    def __init__(self, descricao, motorista, veiculo, status):
        Entrega.idcont = int(pegarid("entrega")) + 1
        self.id = Entrega.idcont
        self.descricao = descricao
        self.__motorista = motorista
        self.__veiculo = veiculo
        self.__status = status
        
    def __str__(self):
        return f"{self.id} - {self.descricao} - {self.__motorista} - {self.__veiculo} - {self.__status}"
    
    @property
    def motorista(self):
        return self.__motorista
    
    @property
    def veiculo(self):
        return self.__veiculo
    
    @property
    def status(self):
        return self.__status

    #verificar se o status é OK
    @status.setter
    def status(self, status):
        self.__status = status    
    #python nao aceita chamar função em objetos de classes privados, ou seja, essa função é necessaria
    def para_dicionario(self):
        dic = {
            str(self.id): {
                "descricao": self.descricao,
                "motorista": self.motorista.todict(),
                "veiculo": self.veiculo.todict(),
                "status": self.__status
            }
        }
        return dic
    
    @staticmethod
    def registrar_entrega():
        descricao = input("Descricao: ")
        motoristas = pegarinformacoes("motorista")
        
        if motoristas == {}:
            print("Nenhum motorista cadastrado!")
            input("Pressione enter para continuar...")

            return False
        else:
            print("Motoristas cadastrados: ")
            
            for i in range(len(motoristas)):
                print(f"{i+1} - {motoristas[str(i+1)]['nome']} - {motoristas[str(i+1)]['cnh']}")
                
            while True:
                try:
                    motorista_escolhido = int(input("Escolha o motorista pelo numero dele: "))
                    if motorista_escolhido > len(motoristas) or motorista_escolhido < 1:
                        input("[ERRO] Número não encontrado!, Pressione enter para continuar...")
                        continue
                except:
                    input("[ERRO] Opção inválida!, Pressione enter para continuar...")
                    continue
                else:
                    for i in range(len(motoristas)):
                        if motorista_escolhido == i+1:
                            motorista_escolhido = motoristas[str(i+1)]
                            id_motorista_escolhido = str(i+1)
                            input(motorista_escolhido)
                            break
                    break
            veiculos = pegarinformacoes("veiculo")
            
            if veiculos == {}:
                print("Nenhum veículo cadastrado!")
                input("Pressione enter para continuar...")
                return False
            else:
                print("Veículos cadastrados: ")
                for i in range(len(veiculos)):
                    print(f"{i+1} - {veiculos[str(i+1)]['modelo']} - {veiculos[str(i+1)]['placa']}")
                while True:
                    try:
                        veiculo_escolhido = int(input("Escolha o veículo pelo numero dele: "))
                        if veiculo_escolhido > len(veiculos) or veiculo_escolhido < 1:
                            input("[ERRO] Número não encontrado!, Pressione enter para continuar...")
                            continue
                    except:
                        input("[ERRO] Opção inválida!, Pressione enter para continuar...")
                        continue
                    else:
                        for i in range(len(veiculos)):
                            if veiculo_escolhido == i+1:
                                veiculo_escolhido = veiculos[str(i+1)]
                                id_veiculo_escolhido = str(i+1)
                                input(veiculo_escolhido)
                                break
                        break
                    
                status = input("Status da entrega: ")
                motorista = Motorista.toobj(motorista_escolhido)
                veiculo = Veiculo.toobj(veiculo_escolhido)
                motorista.id = id_motorista_escolhido
                veiculo.id = id_veiculo_escolhido
                entrega = Entrega(descricao, motorista, veiculo, status)
                salvarinformacoes("entrega", entrega.para_dicionario())
            #VER COMO VAI FUNCIONAR ESSA TRANSFERENCIA DE DADOS
            #JSON PRIMEIRO E DEPOIS CLASSE, OU AO CONTRARIO
                print("====ENTREGA REGISTRADA COM SUCESSO====")
                input("Pressione enter para continuar...")
                return True
if __name__ == "__main__":
    Entrega.registrar_entrega()
    