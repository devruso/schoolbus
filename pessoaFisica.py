from pessoa import Pessoa
class PessoaFisica(Pessoa):
    def __init__(self, nome_oficial, cpf_cnpj, endereco, telefone,nome,mae,pai,naturalidade,data_nascimento):
        super().__init__(nome_oficial, cpf_cnpj, endereco, telefone)
        self._nome = nome
        self._mae = mae
        self._pai = pai
        self._naturalidade = naturalidade
        self._data_nascimento = data_nascimento

    def exibirDados(self):
        return super().exibirDados() + f"Nome Social: {self._nome}\nMãe: {self._mae}\nPai: {self._pai}\nNaturalidade: {self._naturalidade}\nData de Nascimento: {self._data_nascimento}\n"

    def verificarTipo(self):
        return "Pessoa Física"
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def mae(self):
        return self._mae
    @mae.setter
    def mae(self, mae):
        self._mae = mae


    @property
    def pai(self):
        return self._pai
    @pai.setter
    def pai(self, pai):
        self._pai = pai

    @property
    def naturalidade(self):
        return self._naturalidade
    @naturalidade.setter
    def naturalidade(self, naturalidade):
        self._naturalidade = naturalidade

    @property
    def data_nascimento(self):
        return self._data_nascimento
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento
