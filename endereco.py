class Endereco:
    def __init__(self, rua, numero, bairro, complemento):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.complemento = complemento

    def getRua(self):
        return self.rua

    def getNumero(self):
        return self.numero

    def getBairro(self):
        return self.bairro

    def getComplemento(self):
        return self.complemento

    def setRua(self, rua):
        self.rua = rua

    def setNumero(self, numero):
        self.numero = numero

    def setBairro(self, bairro):
        self.bairro = bairro

    def setComplemento(self, complemento):
        self.complemento = complemento
    
    def __str__(self):
        return f"Rua: {self.rua}\nNumero: {self.numero}\nBairro: {self.bairro}\nComplemento: {self.complemento}\n"