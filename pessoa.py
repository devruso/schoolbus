class Pessoa:
    def __init__(self, nome_oficial, cpf, endereco, telefone):
        self.nome_oficial = nome_oficial
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

    def getNome_oficial(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nCPF: {self.cpf}\nEndereco: {self.endereco}\nTelefone: {self.telefone}\n"

    def verificarTipo(self):
        return "Pessoa"
    