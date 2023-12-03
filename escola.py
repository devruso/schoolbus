class Escola(PessoaJuridica):
    def __init__(self,nome_oficial,cpf_cnpj,endereco,telefone,nome_fantasia, num_funcionarios,alunos):
        super().__init__(nome_oficial,cpf_cnpj,endereco,telefone,nome_fantasia,num_funcionarios)
        self.alunos = alunos
    
    def exibirDados(self):
        return super().exibirDados() + f"Alunos: {self.alunos}\n"
    
    def verificarTipo(self):
        return "Escola"

    def matricularAluno(self,aluno):
        self.alunos.append(aluno)
    def desmatricularAluno(self,aluno):
        self.alunos.remove(aluno)

    def exibirAlunos(self):
        for aluno in self.alunos:
            print(aluno.exibirDados())
        
    
        