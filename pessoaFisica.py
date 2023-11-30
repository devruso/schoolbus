class PessoaFisica(Pessoa):
    def __init__(self, nome_oficial, cpf, endereco, telefone,nome,mae,pai,naturalidade,data_nascimento):
        super().__init__(nome_oficial, cpf, endereco, telefone)
        self.nome = nome
        self.mae = mae
        self.pai = pai
        self.naturalidade = naturalidade
        self.data_nascimento = data_nascimento

    def exibirDados(self):
        return super().exibirDados() + f"Nome: {self.nome}\n Mãe: {self.mae}\n Pai: {self.pai}\n Naturalidade: {self.naturalidade}\n Data de Nascimento: {self.data_nascimento}\n"

    def verificarTipo(self):
        return "Pessoa Física"
    
    @nome.getter
    def nome(self):
        return self.nome
    @nome.setter
    def nome(self, nome):
        self.nome = nome

    @mae.getter
    def mae(self):
        return self.mae
    @mae.setter
    def mae(self, mae):
        self.mae = mae


    @pai.getter
    def pai(self):
        return self.pai
    @pai.setter
    def pai(self, pai):
        self.pai = pai

    @naturalidade.getter
    def naturalidade(self):
        return self.naturalidade
    @naturalidade.setter
    def naturalidade(self, naturalidade):
        self.naturalidade = naturalidade

    @data_nascimento.getter
    def data_nascimento(self):
        return self.data_nascimento
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.data_nascimento = data_nascimento
