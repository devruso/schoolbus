class Contrato:
    def __init__(self, num_contrato, data_inicio, data_fim, valor, motoristas, veiculos, fornecedor):
        self.num_contrato = num_contrato
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.valor = valor
        self.motoristas = motoristas
        self.veiculos = veiculos
        self.fornecedor = fornecedor

    def exibirDados(self):
        return f"Número do Contrato: {self.num_contrato}\n Data de Início: {self.data_inicio}\n Data de Fim: {self.data_fim}\n Valor: {self.valor}\n Motoristas: {self.motoristas}\n Veículos: {self.veiculos}\n Fornecedor: {self.fornecedor}\n"
    
    def isTerceirizado(self):
        return self.motorista.isTerceirizado()
    
    @num_contrato.setter
    def num_contrato(self, num_contrato):
        self.num_contrato = num_contrato
    @num_contrato.getter
    def num_contrato(self):
        return self.num_contrato

    @data_inicio.setter
    def data_inicio(self, data_inicio):
        self.data_inicio = data_inicio
    @data_inicio.getter
    def data_inicio(self):
        return self.data_inicio

    @data_fim.setter
    def data_fim(self, data_fim):
        self.data_fim = data_fim
    @data_fim.getter
    def data_fim(self):
        return self.data_fim

    @valor.setter
    def valor(self, valor):
        self.valor = valor
    @valor.getter
    def valor(self):
        return self.valor
    
    @tipo_contrato.setter
    def tipo_contrato(self, tipo_contrato):
        self.tipo_contrato = tipo_contrato

    @motoristas.setter
    def motoristas(self, motoristas):
        self.motoristas = motoristas
    @motoristas.getter
    def motoristas(self):
        return self.motoristas
    
    @fornecedor.setter
    def fornecedor(self, fornecedor):
        self.fornecedor = fornecedor
    @fornecedor.getter
    def fornecedor(self):
        return self.fornecedor
    
    def adicionarMotorista(self, motorista):
        if motorista not in self.motoristas:
            self.motoristas.append(motorista)
        else:
            print("Motorista já cadastrado")
    def removerMotorista(self, motorista):
        self.motoristas.remove(motorista)
    
    def adicionarVeiculo(self, veiculo):
        if veiculo not in self.veiculos:
            self.veiculos.append(veiculo)
        else:
            print("Veículo já cadastrado")
    def removerVeiculo(self, veiculo):
        self.veiculos.remove(veiculo)
    
