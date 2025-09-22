# from utils import pegarid, salvarinformacoes, pegarinformacoes
# def checar_placa(placa):
#     if len(placa) != 7:
#         return False
#     dados = pegarinformacoes("veiculo")
#     for k,j in dados.items():
#         if j["placa"] == placa:
#             return "existe"
#     else:
#         return True
    
# class Veiculo():
#     idcont = 1
#     def __init__(self, placa, modelo):
#         Veiculo.idcont = int(pegarid("veiculo"))
#         self.id = Veiculo.idcont +1
#         Veiculo.idcont += 1
#         self.__placa = placa
#         self.modelo = modelo
#     def __str__(self):
#         return f"{self.id} - {self.__placa} - {self.modelo}"

#     @property
#     def placa(self):
#         return self.__placa

#     @placa.setter
#     def placa(self, placa):
#         self.__placa = placa

#     @staticmethod
#     def todict(objeto):
#         return {"id":str(objeto.id), "placa":str(objeto.placa), "modelo":str(objeto.modelo)}
#     @classmethod
#     def criar_veiculo(cls):
#         placa = input("Placa: ")
#         while checar_placa(placa) == False or checar_placa(placa) == "existe" or placa == "0":
#             if checar_placa(placa) == "existe":
#                 print("Placa ja cadastrada")
#             if placa == "0":
#                 return False
#             placa = input("Placa incorreta, informe corretamente, ou 0 para cancelar e sair: ")
#         modelo = input("Modelo: ")
        
#         a = cls(placa, modelo)
#         salvarinformacoes("veiculo",Veiculo.todict(a))
#         return True


# if __name__ == "__main__":
#     print(Veiculo.criar_veiculo())

from utils import pegarid, salvarinformacoes, pegarinformacoes
import re

class Veiculo():
    def __init__(self, placa, modelo):
        self.id = None
        self.placa = placa
        self.modelo = modelo

    def __str__(self):
        return f"{self.id} - {self.modelo} - Placa: {self.placa}"
    
    @staticmethod
    def validando (placa):
        antigo = r"^[A-Z]{3}[0-9]{4}$"
        mercosul = r"^[A-Z]{3}[0-9][A-Z][0-9]{2}$"
        return bool(re.match(antigo, placa.upper()) or re.match(mercosul, placa.upper()))
    
    @staticmethod
    def cadastrar ():
        veiculos = pegarinformacoes("veiuculo")
        modelo = input("Modelo so veículo: ")

        while True:
            placa = input("Placa do veículo: ").upper()
            if Veiculo.validando(placa):
                veiculos = pegarinformacoes("veiculo")
                if not veiculos:
                    veiculos = {}

                novoid = pegarid("veiculo") + 1
                v = Veiculo(placa, modelo)
                v.id = novoid

                veiculos[str(v.id)] = {"modelo": v.modelo, "placa": v.placa}
                salvarinformacoes("veiculo", veiculos)

                print("==== VEÍCULO CADASTRADO COM SUCESSO ====")
                break
            else:
                print("[ERRO] Placa inválida!")

