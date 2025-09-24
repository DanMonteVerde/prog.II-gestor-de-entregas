from utils import pegarid, pegarinformacoes, salvarinformacoes
from motoristas import Motorista
from veiculo import Veiculo
class Entrega():
    idcont = 1
    def __init__(self, descricao, motorista, veiculo, status):
        Entrega.idcont = int(pegarid("entrega"))
        self.id = Entrega.idcont+1
        Entrega.idcont += 1
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
if __name__ == "__main__":
    Entrega.registrar_entrega()
    