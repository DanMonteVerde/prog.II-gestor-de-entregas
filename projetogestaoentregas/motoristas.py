
class Motorista():
    idcont = 1
    def __init__(self, id, nome, cnh):
        self.id = Motorista.idcont
        Motorista.idcont +=1
        self.nome = nome
        self.cnh = cnh
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.cnh}"
