class Rota:
    _rotasCriadas = 0
    _id = 0
    def __init__(self, id, pontosDeParada):
        self._id = Rota._id
        self._pontosDeParada = pontosDeParada
        Rota._rotasCriadas += 1
        Rota._id += 1
        
    @property
    def rotasCriadas(self):
        return Rota._rotasCriadas
    
    def demandaTotal(self):
        demanda = 0
        for ponto in self._pontosDeParada:
            demanda += 1
        return demanda
    
    def adicionarPontoDeParada(self, pontoDeParada):
        self._pontosDeParada.append(pontoDeParada)
    