class Motorista(PessoaFisica):
    def __init__(self, nome_oficial, cpf_cnpj, data_nascimento, num_habilitacao, terceirizado, num_contrato):
        super().__init__(nome_oficial, cpf_cnpj, data_nascimento)
        self.num_habilitacao = num_habilitacao
        self.terceirizado = terceirizado
        self.num_contrato = num_contrato
    
    def exibirDados(self):
        return super().exibirDados() + f"Número da Habilitação: {self.num_habilitacao}\n Terceirizado: {self.terceirizado}\n Número do Contrato: {self.num_contrato}\n"
    
    def verificarTipo():
        return "Motorista"
    
    @terceirizado.getter
    def terceirizado(self):
        return self.terceirizado
    @terceirizado.setter
    def terceirizado(self, terceirizado):
        self.terceirizado = terceirizado

    @num_contrato.getter
    def num_contrato(self):
        return self.num_contrato
    @num_contrato.setter
    def num_contrato(self, num_contrato):
        self.num_contrato = num_contrato

    @num_habilitacao.getter
    def num_habilitacao(self):
        return self.num_habilitacao
    @num_habilitacao.setter
    def num_habilitacao(self, num_habilitacao):
        self.num_habilitacao = num_habilitacao
    

    