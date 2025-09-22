from utils import pegarid, salvarinformacoes, pegarinformacoes
def checar_placa(placa):
    if len(placa) != 7:
        return False
    dados = pegarinformacoes("veiculo")
    for k,j in dados.items():
        if j["placa"] == placa:
            return "existe"
    else:
        return True
class Veiculo():
    idcont = 1
    def __init__(self, placa, modelo):
        Veiculo.idcont = int(pegarid("veiculo"))
        self.id = Veiculo.idcont +1
        Veiculo.idcont += 1
        self.__placa = placa
        self.modelo = modelo
    def __str__(self):
        return f"{self.id} - {self.__placa} - {self.modelo}"

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa):
        self.__placa = placa

    @staticmethod
    def todict(objeto):
        return {"id":str(objeto.id), "placa":str(objeto.placa), "modelo":str(objeto.modelo)}
    @classmethod
    def criar_veiculo(cls):
        placa = input("Placa: ")
        while checar_placa(placa) == False or checar_placa(placa) == "existe" or placa == "0":
            if checar_placa(placa) == "existe":
                print("Placa ja cadastrada")
            if placa == "0":
                return False
            placa = input("Placa incorreta, informe corretamente, ou 0 para cancelar e sair: ")
        modelo = input("Modelo: ")
        
        a = cls(placa, modelo)
        salvarinformacoes("veiculo",Veiculo.todict(a))
        return True


if __name__ == "__main__":
    print(Veiculo.criar_veiculo())