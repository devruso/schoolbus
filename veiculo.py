class Veiculo:
    def __init__(self, placa, ano, modelo, capacidade, isAlugado, contrato):
        self.placa = placa
        self.ano = ano
        self.modelo = modelo
        self.capacidade = capacidade
        self.isAlugado = isAlugado
        self.contrato = contrato
    
    @isAlugado.getter
    def isAlugado(self):
        return self.isAlugado
    @isAlugado.setter
    def isAlugado(self, isAlugado):
        self.isAlugado = isAlugado
    
    @contrato.getter
    def contrato(self):
        return self.contrato
    @contrato.setter
    def contrato(self, contrato):
        self.contrato = contrato