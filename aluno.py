from pessoaFisica import PessoaFisica
class Aluno(PessoaFisica):
    def __init__(self, nome_oficial, cpf_cnpj, endereco, telefone, nome, mae, pai, naturalidade, data_nascimento, escola, matricula, turno, serie, pontoDeParada):
        super().__init__(nome_oficial, cpf_cnpj, endereco, telefone, nome, mae, pai, naturalidade, data_nascimento)
        self._escola = escola
        self._matricula = matricula
        self._turno = turno
        self._serie = serie
        self._pontoDeParada = pontoDeParada
    
    
    def exibirDados(self):
        return super().exibirDados() + f"Escola: {self._escola.exibirDados()}\nMatrícula: {self._matricula}\nTurno: {self._turno}\nSerie: {self._serie} \nPonto de Parada: {self._pontoDeParada.exibirDados()}\n"

    def verificarTipo(self):
        return "Aluno"
    
    @property
    def escola(self):
        return self._escola
    @escola.setter
    def escola(self, escola):
        self._escola = escola
    
    @property
    def matricula(self):
        return self._matricula
    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @property
    def turno(self):
        return self._turno
    @turno.setter
    def turno(self, turno):
        self._turno = turno
    
    @property
    def pontoDeParada(self):
        return self._pontoDeParada
    @pontoDeParada.setter
    def pontoDeParada(self, pontoDeParada):
        self._pontoDeParada = pontoDeParada
