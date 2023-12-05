from pessoaJuridica import PessoaJuridica
class Fornecedor(PessoaJuridica):
    def __init__(self,nome_oficial,cpf_cnpj,endereco,telefone,nome_fantasia,num_funcionarios):
        super().__init__(nome_oficial,cpf_cnpj,endereco,telefone,nome_fantasia,num_funcionarios)
        self._contratos = []
    
    def exibirDados(self):
        return super().exibirDados() + f"\nContratos: {self._contratos}\n"
    
    def verificarTipo(self):
        return "Fornecedor"

    def adicionarContrato(self, contrato):
        self._contratos.append(contrato)