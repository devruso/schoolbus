class Aluno(PessoaFisica):
    def __init__(self, nome_oficial, cpf, endereco, telefone,nome,mae,pai,naturalidade,data_nascimento,escola,matricula,turno,pontoDeParada):
        super().__init__(nome_oficial, cpf, endereco, telefone,nome,mae,pai,naturalidade,data_nascimento)
        self.escola = escola
        self.matricula = matricula
        self.turno = turno
        self.pontoDeParada = pontoDeParada
    
    
    def exibirDados(self):
        return super().exibirDados() + f"Escola: {self.escola}\n Matrícula: {self.matricula}\n Turno: {self.turno}\n Ponto de Parada: {self.pontoDeParada}\n"

    def verificarTipo(self):
        return "Aluno"
    
    @escola.getter
    def escola(self):
        return self.escola
    @escola.setter
    def escola(self, escola):
        self.escola = escola
    
    @matricula.getter
    def matricula(self):
        return self.matricula
    @matricula.setter
    def matricula(self, matricula):
        self.matricula = matricula

    @turno.getter
    def turno(self):
        return self.turno
    @turno.setter
    def turno(self, turno):
        self.turno = turno
    
    @pontoDeParada.getter
    def pontoDeParada(self):
        return self.pontoDeParada
    @pontoDeParada.setter
    def pontoDeParada(self, pontoDeParada):
        self.pontoDeParada = pontoDeParada
