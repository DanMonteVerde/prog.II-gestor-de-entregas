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
    def validando(placa):
        antigo = r"^[A-Z]{3}[0-9]{4}$"
        mercosul = r"^[A-Z]{3}[0-9][A-Z][0-9]{2}$"
        return bool(re.match(antigo, placa.upper()) or re.match(mercosul, placa.upper()))
    
    @staticmethod
    def cadastrar():
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

