from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome_oficial, cpf_cnpj, endereco, telefone):
        self._nome_oficial = nome_oficial
        self._cpf_cnpj = cpf_cnpj
        self._endereco = endereco
        self._telefone = telefone

    @property
    def nome_oficial(self):
        return self._nome_oficial

    @nome_oficial.setter
    def nome_oficial(self, nome_oficial):
        self._nome_oficial = nome_oficial
    
    def exibirDados(self):
        return f"Nome Oficial: {self._nome_oficial}\nCPF: {self._cpf_cnpj}\nEndereco: {self._endereco.exibirDados()}\nTelefone: {self._telefone}\n"
    
    @abstractmethod
    def verificarTipo(self):
        pass
    