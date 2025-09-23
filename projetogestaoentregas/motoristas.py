from utils import pegarinformacoes, salvarinformacoes, pegarid
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
    

    @staticmethod
    
    def cadastrar():
        
        motoristas = pegarinformacoes("motorista")

        nome = input("Nome do motorista: ")

        while True:
            cnh = input("CNH (11 dígitos): ")
            if Motorista.valida_cnh(cnh):
                novo_id = pegarid("motorista") + 1
                m = Motorista(nome, cnh)
                m.id = novo_id

                motoristas[str(m.id)] = {"nome": m.nome, "cnh": m.cnh}
                salvarinformacoes("motorista", motoristas)

                print("====MOTORISTA CADASTRADO COM SUCESSO====")
                break
            else:
                print("[ERRO] CNH INVÁLIDA!")


if __name__ == "__main__":
    e = Motorista("","")
    print(e)