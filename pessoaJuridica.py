from pessoa import Pessoa
class PessoaJuridica(Pessoa):
    def __init__(self,nome_oficial, cpf_cnpj, endereco, telefone, nome_fantasia, num_funcionarios):
        super().__init__(nome_oficial, cpf_cnpj, endereco, telefone)
        self._nome_fantasia = nome_fantasia
        self._num_funcionarios = num_funcionarios
    
    def exibirDados(self):
        return super().exibirDados() + f"Nome Fantasia: {self._nome_fantasia}\nNúmero de Funcionários: {self._num_funcionarios}\n"

    def verificarTipo(self):
        return "Pessoa Jurídica"
    
    @property
    def nome_fantasia(self):
        return self._nome_fantasia
    @nome_fantasia.setter
    def nome_fantasia(self, nome_fantasia):
        self._nome_fantasia = nome_fantasia
    
    @property
    def num_funcionarios(self):
        return self._num_funcionarios
    @num_funcionarios.setter
    def num_funcionarios(self, num_funcionarios):
        self._num_funcionarios = num_funcionarios
