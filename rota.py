class Rota:
    rotasCriadas = 0
    id = 0
    def __init__(self, id, pontosDeParada):
        self.id = Rota.id
        self.pontosDeParada = pontosDeParada
        Rota.rotasCriadas += 1
        Rota.id += 1
    
    def rotasCriadas(self):
        return Rota.rotasCriadas
    
    def demandaTotal(self):
        demanda = 0
        for ponto in self.pontosDeParada:
            demanda += ponto.demanda
        return demanda