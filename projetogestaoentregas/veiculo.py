class Veiculo():
    idcont = 1
    def __init__(self, id, placa, modelo):
        self.id = Veiculo.idcont
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
    