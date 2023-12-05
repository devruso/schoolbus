class PontoDeParada:
    _totalDeParadas = 0

    def __init__(self,nome,latitude,longitude):
        self._nome = nome
        self._latitude = latitude
        self._longitude = longitude
        self._alunos = []
        PontoDeParada._totalDeParadas += 1

    def adicionarAluno(self, aluno):
        self._alunos.append(aluno)
    
    @property
    def get_totalDeParadas(self):
        return PontoDeParada._totalDeParadas

    def lerAlunos(self):
        for aluno in self._alunos:
            print(aluno.exibirDados())

    def exibirDados(self):
        return f"Nome: {self._nome}\nLatitude: {self._latitude}\nLongitude: {self._longitude}\nAlunos: {self._alunos}\nTotal de Paradas: {PontoDeParada._totalDeParadas}\n"

    