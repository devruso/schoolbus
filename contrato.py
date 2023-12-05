class Contrato:
    def __init__(self, num_contrato, data_inicio, data_fim, valor, fornecedor):
        self._num_contrato = num_contrato
        self._data_inicio = data_inicio
        self._data_fim = data_fim
        self._valor = valor
        self._fornecedor = fornecedor
        self._motoristas = []
        self._veiculos = []

    def exibirDados(self):
        return f"Número do Contrato: {self.num_contrato}\n Data de Início: {self.data_inicio}\n Data de Fim: {self.data_fim}\n Valor: {self.valor}\n Motoristas: {self.motoristas}\n Veículos: {self.veiculos}\n Fornecedor: {self.fornecedor}\n"
    
    def isTerceirizado(self):
        return self.motorista.isTerceirizado()
    
    @property
    def num_contrato(self):
        return self._num_contrato
    @num_contrato.setter
    def num_contrato(self, num_contrato):
        self._num_contrato = num_contrato

    @property
    def data_inicio(self):
        return self._data_inicio
    @data_inicio.setter
    def data_inicio(self, data_inicio):
        self._data_inicio = data_inicio

    @property
    def data_fim(self):
        return self._data_fim
    @data_fim.setter
    def data_fim(self, data_fim):
        self._data_fim = data_fim

    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self, valor):
        self._valor = valor
    
    @property
    def tipo_contrato(self):
        return self._tipo_contrato
    @tipo_contrato.setter
    def tipo_contrato(self, tipo_contrato):
        self._tipo_contrato = tipo_contrato

    @property
    def motoristas(self):
        return self._motoristas
    @motoristas.setter
    def motoristas(self, motoristas):
        self._motoristas = motoristas
    
    @property
    def fornecedor(self):
        return self._fornecedor
    @fornecedor.setter
    def fornecedor(self, fornecedor):
        self._fornecedor = fornecedor
    
    def adicionarMotorista(self, motorista):
        if motorista not in self._motoristas:
            self._motoristas.append(motorista)
        else:
            print("Motorista já cadastrado")
    def removerMotorista(self, motorista):
        self._motoristas.remove(motorista)
    
    def adicionarVeiculo(self, veiculo):
        if veiculo not in self._veiculos:
            self._veiculos.append(veiculo)
        else:
            print("Veículo já cadastrado")
    def removerVeiculo(self, veiculo):
        self._veiculos.remove(veiculo)
    
