class PessoaJuridica(Pessoa):
    def __init__(self,nome_oficial, cpf_cnpj, endereco, telefone, nome_fantasia, num_funcionarios):
        super().__init__(nome_oficial, cpf_cnpj, endereco, telefone)
        self.nome_fantasia = nome_fantasia
        self.num_funcionarios = num_funcionarios
    
    def exibirDados(self):
        return super().exibirDados() + f"Nome Fantasia: {self.nome_fantasia}\n Número de Funcionários: {self.num_funcionarios}\n"

    def verificarTipo(self):
        return "Pessoa Jurídica"
    
    @nome_fantasia.getter
    def nome_fantasia(self):
        return self.nome_fantasia
    @nome_fantasia.setter
    def nome_fantasia(self, nome_fantasia):
        self.nome_fantasia = nome_fantasia
    
    @num_funcionarios.getter
    def num_funcionarios(self):
        return self.num_funcionarios
    @num_funcionarios.setter
    def num_funcionarios(self, num_funcionarios):
        self.num_funcionarios = num_funcionarios
