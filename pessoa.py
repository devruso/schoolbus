from ABC import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome_oficial, cpf, endereco, telefone):
        self.nome_oficial = nome_oficial
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

    @nome_oficial.getter
    def nome_oficial(self):
        return self.nome

    @nome_oficial.setter
    def nome_oficial(self, nome):
        self.nome_oficial = nome

    @idade.geter
    def idade(self):
        return self.idade
    @idade.setter
    def idade(self, idade):
        self.idade = idade
    
    def exibirDados(self):
        return f"Nome: {self.nome}\n Idade: {self.idade}\n CPF: {self.cpf}\n Endereco: {self.endereco}\n Telefone: {self.telefone}\n"
    
    @abstractmethod
    def verificarTipo(self):
        pass
    