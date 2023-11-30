class PontoDeParada:
    totalDeParadas = 0
    def __init__(self,nome,latitude,longitude, alunos = [], totalDeParadas = 0):
        self.nome = nome
        self.latitude = latitude
        self.longitude = longitude
        self.alunos = alunos if alunos is not None else []
        PontoDeParada.totalDeParadas += 1

    def adicionarAluno(self, aluno):
        self.alunos.append(aluno)
    
    @totalDeParadas.getter
    def totalDeParadas(self):
        return PontoDeParada.totalDeParadas

    def apresentarDados(self):
        return f"Nome: {self.nome}\n Latitude: {self.latitude}\n Longitude: {self.longitude}\n Alunos: {self.alunos}\n Total de Paradas: {self.totalDeParadas}\n"

    