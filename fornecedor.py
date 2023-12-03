class Fornecedor(PessoaJuridica):
    def __init__(self,nome_oficial,cpf_cnpj,endereco,telefone,nome_fantasia,num_funcionarios, contratos):
        super().__init__(nome_oficial,cpf_cnpj,endereco,telefone,nome_fantasia,num_funcionarios)
        self.contratos = contratos
    
    def exibirDados(self):
        return f"Nome Oficial: {self.nome_oficial}\n CNPJ: {self.cpf_cnpj}\n Endereço: {self.endereco}\n Telefone: {self.telefone}\n Nome Fantasia: {self.nome_fantasia}\n Número de Funcionários: {self.num_funcionarios}\n Contratos: {self.contratos}\n"
    
    def verificarTipo(self):
        return "Fornecedor"

    def adicionarContrato(self, contrato):
        self.contratos.append(contrato)