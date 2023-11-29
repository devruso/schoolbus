from ABC import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome_oficial, cpf, endereco, telefone):
        self.nome_oficial = nome_oficial
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

    @property
    def nome_oficial(self):
        return self.nome

    @nome_oficial.setter
    def nome_oficial(self, nome):
        self.nome_oficial = nome

    @property
    def idade(self):
        return self.idade
    @idade.setter
    def idade(self, idade):
        self.idade = idade
    
    def __str__(self):
        return f"Nome: {self.nome}\n Idade: {self.idade}\n CPF: {self.cpf}\n Endereco: {self.endereco}\n Telefone: {self.telefone}\n"
    
    @abstractmethod
    def verificarTipo(self):
        pass
    