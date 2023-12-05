class Veiculo:
    def __init__(self, placa, ano, modelo, capacidade, isAlugado, contrato):
        self._placa = placa
        self._ano = ano
        self._modelo = modelo
        self._capacidade = capacidade
        self._isAlugado = isAlugado
        self._contrato = contrato
    
    @property
    def isAlugado(self):
        return self._isAlugado
    @isAlugado.setter
    def isAlugado(self, isAlugado):
        self._isAlugado = isAlugado
    
    @property
    def contrato(self):
        return self._contrato
    @contrato.setter
    def contrato(self, contrato):
        self._contrato = contrato