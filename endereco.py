class Endereco:
    def __init__(self, rua, numero, bairro, complemento):
        self._rua = rua
        self._numero = numero
        self._bairro = bairro
        self._complemento = complemento

    def getRua(self):
        return self._rua

    def getNumero(self):
        return self._numero

    def getBairro(self):
        return self._bairro

    def getComplemento(self):
        return self._complemento

    def setRua(self, rua):
        self._rua = rua

    def setNumero(self, numero):
        self._numero = numero

    def setBairro(self, bairro):
        self._bairro = bairro

    def setComplemento(self, complemento):
        self._complemento = complemento
    
    def exibirDados(self):
        return f"\nRua: {self._rua}\nNumero: {self._numero}\nBairro: {self._bairro}\nComplemento: {self._complemento}\n"