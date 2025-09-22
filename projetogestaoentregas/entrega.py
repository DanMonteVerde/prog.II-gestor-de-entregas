from utils import pegarid
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
    def status(self):
        return self.__status

    #verificar se o status é OK
    @status.setter
    def status(self, status):
        self.__status = status    

if __name__ == "__main__":
    e = Entrega("","","","")
    print(e)