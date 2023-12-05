from abc import ABC, abstractmethod
from pessoa import Pessoa
from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica
from endereco import Endereco
from escola import Escola
from pontoDeParada import PontoDeParada
from aluno import Aluno
from motorista import Motorista
from contrato import Contrato
from fornecedor import Fornecedor
from veiculo import Veiculo
from rota import Rota


class Menu:
    def __init__(self):
        self.opcao = 0

    def exibir_menu(self):
        print("1 - Cadastrar Endereco")
        print("2 - Cadastrar Escola")
        print("3 - Cadastrar Ponto de Parada")
        print("4 - Cadastrar Aluno")
        print("5 - Cadastrar Motorista")
        print("6 - Cadastrar Contrato")
        print("7 - Cadastrar Fornecedor")
        print("8 - Cadastrar Veiculo")
        print("9 - Cadastrar Rota")
        print("10 - Calcular demanda total de uma rota")
        print("11 - Exibir total de rotas")
        print("12 - Exibir total de pontos de parada")
        print("13 - Exibir tipo de pessoa")
        print("14 - Exibir informações detalhadas")
        print("16 - Sair")

    def obter_opcao(self):
        return int(input("Digite a opção desejada: "))

menu = Menu()

enderecos = []
alunos = []
motoristas = []
escolas = []
contratos = []
fornecedores = []
veiculos = []
rotas = []
pontosDeParada = []

def cadastrar_endereco():
    print("\nCadastrar Endereco")
    rua = input("Digite a rua: ")
    numero = input("Digite o número: ")
    bairro = input("Digite o bairro: ")
    complemento = input("Digite o complemento: ")
    endereco = Endereco(rua, numero, bairro, complemento)
    enderecos.append(endereco)
    print("Endereço cadastrado com sucesso\n")
    return endereco

def cadastrar_escola():
    print("\nCadastrar Escola")
    nome_oficial = input("Digite o nome da escola: ")
    cpf_cnpj = input("Digite o CNPJ da escola: ")
    endereco = cadastrar_endereco()
    telefone = input("Digite o telefone da escola: ")
    nome_fantasia = input("Digite o nome fantasia da escola: ")
    num_funcionarios = input("Digite o número de funcionários da escola: ")
    alunos = []
    escola = Escola(nome_oficial, cpf_cnpj, endereco, telefone, nome_fantasia, num_funcionarios, alunos)
    escolas.append(escola)
    print("Escola cadastrada com sucesso\n")
    return escola

def cadastrar_ponto_de_parada():
    print("\nCadastrar Ponto de Parada")
    nome = input("Digite o nome do ponto de parada: ")
    latitude = input("Digite a latitude do ponto de parada: ")
    longitude = input("Digite a longitude do ponto de parada: ")
    pontoDeParada = PontoDeParada(nome, latitude, longitude)
    """
    opcao = 0
    while opcao != 2:
        opcao = int(input("\nDigite 1 para cadastrar aluno no ponto de parada ou 2 para sair: \n"))
        if opcao == 1:
            aluno = cadastrar_aluno()
            pontoDeParada.adicionarAluno(aluno)
        else:
            pass
    """
    pontosDeParada.append(pontoDeParada)
    print("Ponto de Parada cadastrado com sucesso\n")
    return pontoDeParada

def cadastrar_aluno():
    print("\nCadastrar Aluno")
    nome_oficial = input("Digite o Nome Civil do aluno: ")
    cpf_cnpj = input("Digite o CPF do aluno: ")
    endereco = cadastrar_endereco()
    telefone = input("Digite o telefone do aluno: ")
    nome = input("Digite o Nome social do aluno: ")
    mae = input("Digite o nome da mãe do aluno: ")
    pai = input("Digite o nome do pai do aluno: ")
    naturalidade = input("Digite a naturalidade do aluno: ")
    data_nascimento = input("Digite a data de nascimento do aluno: ")
    escola = cadastrar_escola()
    matricula = input("Digite a matrícula do aluno: ")
    turno = input("Digite o turno do aluno: ")
    serie = input("Digite a série do aluno: ")
    pontoDeParada = cadastrar_ponto_de_parada()
    aluno = Aluno(nome_oficial, cpf_cnpj, endereco, telefone, nome, mae, pai, naturalidade, data_nascimento, escola, matricula, turno, serie, pontoDeParada)    
    pontoDeParada.adicionarAluno(aluno)
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso\n")
    return aluno

def cadastrar_motorista():
    print("\nCadastrar Motorista")
    nome_oficial = input("Digite o nome civil do motorista: ")
    cpf_cnpj = input("Digite o CPF do motorista: ")
    data_nascimento = input("Digite a data de nascimento do motorista: ")
    endereco = cadastrar_endereco()
    telefone = input("Digite o telefone do motorista: ")
    nome = input("Digite o nome social do motorista: ")
    mae = input("Digite o nome da mãe do motorista: ")
    pai = input("Digite o nome do pai do motorista: ")
    naturalidade = input("Digite a naturalidade do motorista: ")
    cnh = input("Digite a CNH do motorista: ")
    terceirizado = input("Digite true ou false se o motorista for terceirizado: ")
    num_contrato = input("Digite o número do contrato do motorista: ")
    categoriaCnh = input("Digite a categoria da CNH do motorista: ")
    motorista = Motorista(nome_oficial, cpf_cnpj, endereco, telefone, nome, mae, pai, naturalidade, data_nascimento, cnh, terceirizado, num_contrato, categoriaCnh)
    motorista.adicionarCategoria(categoriaCnh)
    motoristas.append(motorista)
    print("Motorista cadastrado com sucesso\n")
    return motorista

def cadastrar_contrato():
    print("\nCadastrar Contrato")
    num_contrato = input("Digite o número do contrato: ")
    data_inicio = input("Digite a data de início do contrato: ")
    data_fim = input("Digite a data de fim do contrato: ")
    valor = input("Digite o valor do contrato: ")
    fornecedor = cadastrar_fornecedor()
    contrato = Contrato(num_contrato, data_inicio, data_fim, valor, fornecedor)
    """
    print("Adicionar ao menos um motorista ao contrato")
    opcao = 0
    while opcao != 2:
        motorista = cadastrar_motorista()
        contrato.adicionarMotorista(motorista)
        contratos.append(contrato)
        opcao = int(input("Digite 1 para adicionar outro motorista ou 2 para sair: "))
    print("Adicionar ao menos um veículo ao contrato\n")
    opcao = 0
    while opcao != 2:
        veiculo = cadastrar_veiculo()
        contrato.adicionarVeiculo(veiculo)
        contratos.append(contrato)
        opcao = int(input("Digite 1 para adicionar outro veículo ou 2 para sair: "))
    print("Contrato cadastrado com sucesso")
    """
    return contrato

def cadastrar_fornecedor():
    print("\nCadastrar Fornecedor")
    nome_oficial = input("Digite o nome oficial do fornecedor: ")
    cpf_cnpj = input("Digite o CPF/CNPJ do fornecedor: ")
    endereco = cadastrar_endereco()
    telefone = input("Digite o telefone do fornecedor: ")
    nome_fantasia = input("Digite o nome fantasia do fornecedor: ")
    num_funcionarios = input("Digite o número de funcionários do fornecedor: ")
    fornecedor = Fornecedor(nome_oficial, cpf_cnpj, endereco, telefone, nome_fantasia, num_funcionarios)
    fornecedores.append(fornecedor)
    print("Fornecedor cadastrado com sucesso\n")
    return fornecedor

def cadastrar_veiculo():

    print("\nCadastrar Veículo")
    placa = input("Digite a placa do veículo: ")
    ano = input("Digite o ano do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    capacidade = input("Digite a capacidade do veículo: ")
    alugado = input("Digite true ou false se o veículo for alugado: ")
    contrato = cadastrar_contrato()
    veiculo = Veiculo(placa,ano, modelo, capacidade, alugado,contrato)
    veiculos.append(veiculo)
    print("Veículo cadastrado com sucesso\n")
    return veiculo

def cadastrar_rota():
    print("\nCadastrar Rota")
    nome = input("Digite o nome da rota: ")
    pontosDeParada = []
    print("Adicionar ao menos um ponto de parada à rota")
    opcao = 0
    while opcao != 2:
        pontoDeParada = cadastrar_ponto_de_parada()
        pontosDeParada.append(pontoDeParada)
        opcao = int(input("Digite 1 para adicionar outro ponto de parada ou 2 para sair: "))
    rota = Rota(nome, pontosDeParada)
    rotas.append(rota)
    print("Rota cadastrada com sucesso\n")
    return rota

def calcular_demanda_total_de_uma_rota():
    if rotas == []:
        print("\nNão há rotas cadastradas")
    else:
        for rota in rotas:
            print(f"\nDemanda total: {rota.demandaTotal()}")

def exibir_total_de_rotas():
    print(f"Há o total de : {Rota._rotasCriadas} rotas criadas")

def exibir_total_de_pontos_de_parada():
    print(f"Há o total de : {PontoDeParada._totalDeParadas} pontos de parada criados")

def exibir_tipo_de_pessoa():
    print("Exibir tipo de pessoas")
    for aluno in alunos:
        print("Nome: " + aluno.nome_oficial)
        print("Tipo: " + aluno.verificarTipo())
        print("CPF ou CNPJ:" + aluno.cpf_cnpj)
    for motorista in motoristas:
        print("Nome: " + motorista.nome_oficial)
        print("Tipo: " + motorista.verificarTipo())
        print("CPF ou CNPJ:" + motorista.cpf_cnpj)
    for escola in escolas:
        print("Nome: " + escola.nome_oficial)
        print("Tipo: " + escola.verificarTipo())
        print("CPF ou CNPJ:" + escola.cpf_cnpj)

def exibir_informacoes_detalhadas():
    print("\nExibir informações detalhadas")
    for aluno in alunos:
        print(aluno.exibirDados())
    for motorista in motoristas:
        print(motorista.exibirDados())
    for escola in escolas:
        print(escola.exibirDados())
    for fornecedor in fornecedores:
        print(fornecedor.exibirDados())
    for veiculo in veiculos:
        print(veiculo.exibirDados())
    for pontoDeParada in pontosDeParada:
        print(pontoDeParada.exibirDados())
    for contrato in contratos:
        print(contrato.exibirDados())


while menu.opcao != 16:
    menu.exibir_menu()
    menu.opcao = menu.obter_opcao()

    if menu.opcao == 1:
        cadastrar_endereco()    
    elif menu.opcao == 2:
        cadastrar_escola()
    elif menu.opcao == 3:
        cadastrar_ponto_de_parada()
    elif menu.opcao == 4:
        cadastrar_aluno()
    elif menu.opcao == 5:
        cadastrar_motorista()
    elif menu.opcao == 6:
        cadastrar_contrato()
    elif menu.opcao == 7:
        cadastrar_fornecedor()
    elif menu.opcao == 8:
        cadastrar_veiculo()
    elif menu.opcao == 9:
        cadastrar_rota()
    elif menu.opcao == 10:
        calcular_demanda_total_de_uma_rota()
    elif menu.opcao == 11:
        exibir_total_de_rotas()
    elif menu.opcao == 12:
        exibir_total_de_pontos_de_parada()
    elif menu.opcao == 13:
        exibir_tipo_de_pessoa()
    elif menu.opcao == 14:
        exibir_informacoes_detalhadas()
    elif menu.opcao == 16:
        print("Saindo...")
   

    