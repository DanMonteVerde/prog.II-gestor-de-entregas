
class Motorista():
    idcont = 1

    def __init__(self, nome:str, cnh:str):
        self.id = Motorista.idcont 
        Motorista.idcont +=1
        self.nome = nome
        self.cnh = cnh

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.cnh}"

    @staticmethod
    def valida_cnh(cnh):
        return cnh.isdigit() and len(cnh) == 11


if __name__ == "__main__":
    e = Motorista("","")
    print(e)