from pessoaFisica import PessoaFisica
class Motorista(PessoaFisica):
    def __init__(self, nome_oficial, cpf_cnpj, data_nascimento,endereco,telefone,nome,mae,pai,naturalidade, num_habilitacao,categorias, terceirizado, num_contrato):
        super().__init__(nome_oficial, cpf_cnpj, data_nascimento,endereco,telefone,nome,mae,pai,naturalidade)
        self._num_habilitacao = num_habilitacao
        self._terceirizado = terceirizado
        self._num_contrato = num_contrato
        self._categorias = []
    
    def exibirDados(self):
        return super().exibirDados() + f"Número da Habilitação: {self._num_habilitacao}\n Terceirizado: {self._terceirizado}\n Número do Contrato: {self._num_contrato}\n"
    
    def verificarTipo():
        return "Motorista"
    
    @property
    def terceirizado(self):
        return self._terceirizado
    @terceirizado.setter
    def terceirizado(self, terceirizado):
        self._terceirizado = terceirizado

    @property
    def num_contrato(self):
        return self._num_contrato
    @num_contrato.setter
    def num_contrato(self, num_contrato):
        self._num_contrato = num_contrato

    @property
    def num_habilitacao(self):
        return self._num_habilitacao
    @num_habilitacao.setter
    def num_habilitacao(self, num_habilitacao):
        self._num_habilitacao = num_habilitacao
    
    def adicionarCategoria(self, categoria):
        self._categorias.append(categoria)
    

    