from negocio import operacoes
import PySimpleGUIQt as sg
import os

class Gui:
    def __init__(self):
        self.BUTTON_PATH = '.'
        self.button_names_main = ('Abastecer', 'Registro', 'Ver Registros', 'Fechar')
        self.button_names_abs = ('Voltar','Calcular','Finalizar')
        self.button_names_abs_veiculo = ('Adicionar', 'Modificar')
        self.button_names_regis_cliente = ('Registrar Cliente', 'Deletar Cliente')
        self.button_names_regis = ('Ok', 'Cancelar')
        self.button_names_cliente = ('Pessoa Física', 'Pessoa Jurídica', 'Tentar Novamente')
        self.button_names_veiculo = ('Novo Veículo', 'Tentar Novamente')
        self.button_names_regis_funcionario = ('Tentar Novamente', 'Cancelar')
        self.button_names_abs_deletar_funcionario = ('Deletar Registro do Funcionário', 'Voltar para Registro')
        self.button_names_ver_registros = ('Mostrar Registros', 'Voltar para Início')
        # botões de crud
        self.button_names_regis_funcionario_crud = ('Criar Funcionário', 'Atualizar Funcionário', 'Voltar para Registro')
        self.button_names_regis_cliente_confirmacao_crud = ('Criar/Atualizar Pessoa Física', 'Criar/Atualizar Pessoa Jurídica', 'Voltar para Registro')
        self.button_names_regis_cliente_crud = ('Criar Cliente', 'Atualizar Cliente', 'Voltar para Registro')
        self.button_names_regis_bandeira_crud = ('Criar Bandeira', 'Atualizar Bandeira', 'Voltar para Registro')
        self.button_names_regis_veiculo_crud = ('Criar Veículo', 'Atualizar Veículo', 'Voltar para Registro')
        self.button_names_regis_combustivel_crud = ('Criar Combustível', 'Atualizar Combustível', 'Voltar para Registro')
        self.button_names_regis_regiao_crud = ('Criar Região', 'Atualizar Região', 'Voltar para Registro')
        self.window = None
        self.window_popup = None

    # toolbar_buttons
    def configToobarBtn(self, lista_btn):

        button_files = [os.path.join(self.BUTTON_PATH, b + '.png') for b in lista_btn]

        toolbar_buttons = [[sg.RButton('{}'.format(lista_btn[i]), image_size=(32, 32), pad=(0, 0),
                                       tooltip=lista_btn[i]) for i, f in enumerate(button_files)], ]
        return toolbar_buttons

    def show(self):
        width = 450
        height = 150

        sg.SetOptions(auto_size_buttons=True, margins=(0, 0), button_color=sg.COLOR_SYSTEM_DEFAULT)

        toolbar_buttons_init = self.configToobarBtn(self.button_names_main)
        toolbar_buttons_abs = self.configToobarBtn(self.button_names_abs)
        toolbar_buttons_abs_veiculo = self.configToobarBtn(self.button_names_abs_veiculo)
        toolbar_buttons_abs_deletar_funcionario = self.configToobarBtn(self.button_names_abs_deletar_funcionario)
        toolbar_buttons_regis = self.configToobarBtn(self.button_names_regis)
        toolbar_buttons_popup = self.configToobarBtn(self.button_names_regis)
        toolbar_buttons_register = self.configToobarBtn(self.button_names_cliente)
        toolbar_buttons_register_veiculo = self.configToobarBtn(self.button_names_veiculo)
        toolbar_buttons_regis_funcionario = self.configToobarBtn(self.button_names_regis_funcionario)
        toolbar_buttons_regis_cliente = self.configToobarBtn(self.button_names_regis_cliente)
        toolbar_buttons_abs_ver_registros = self.configToobarBtn(self.button_names_ver_registros)
        # config botões crud
        toolbar_buttons_regis_funcionario_crud = self.configToobarBtn(self.button_names_regis_funcionario_crud)
        toolbar_buttons_register_cliente_confirmacao_crud = self.configToobarBtn(self.button_names_regis_cliente_confirmacao_crud)
        toolbar_buttons_regis_cliente_crud = self.configToobarBtn(self.button_names_regis_cliente_crud)
        toolbar_buttons_regis_bandeira_crud = self.configToobarBtn(self.button_names_regis_bandeira_crud)
        toolbar_buttons_regis_veiculo_crud = self.configToobarBtn(self.button_names_regis_veiculo_crud)
        toolbar_buttons_regis_combustivel_crud = self.configToobarBtn(self.button_names_regis_combustivel_crud)
        toolbar_buttons_regis_regiao_crud = self.configToobarBtn(self.button_names_regis_regiao_crud)

# Layout
        layout = [
                    [sg.Text("Escolha uma das opções abaixo")],
                    [sg.Frame('', toolbar_buttons_init)]
                 ]

        preco = None
        combustivell = None

        # layouts de escolha
        cadastrosLayout = [
                            [sg.Text('Escolha o que deseja cadastrar:')],
                            [sg.Button('Funcionario')],
                            [sg.Button('Cliente')],
                            [sg.Button('Bandeira')],
                            [sg.Button('Veículo')],
                            [sg.Button('Combustível')],
                            [sg.Button('Região')],
                            [sg.Text('')],
                            [sg.Text('')],
                            [sg.Button('Confirmar'), sg.Button('Voltar para Início')]
        ]

        operacoesFuncionarioLayout = [
                            [sg.Text('Escolha uma operação para fazer:')],
                            [sg.Button('Criar/Atualizar Funcionário')],
                            [sg.Button('Deletar Funcionário')],
                            [sg.Button('Mostrar Funcionário')],
                            [sg.Button('Mostrar Todos Funcionários')],
                            [sg.Button('Voltar para Registro')]
        ]

        operacoesClienteLayout = [
                            [sg.Text('Escolha uma operação para fazer:')],
                            [sg.Button('Criar/Atualizar Cliente')],
                            [sg.Button('Deletar Cliente')],
                            [sg.Button('Mostrar Cliente')],
                            [sg.Button('Mostrar Todos Clientes')],
                            [sg.Button('Voltar para Registro')]
        ]

        operacoesBandeiraLayout = [
                            [sg.Text('Escolha uma operação para fazer:')],
                            [sg.Button('Criar/Atualizar Bandeira')],
                            [sg.Button('Deletar Bandeira')],
                            [sg.Button('Mostrar Bandeira')],
                            [sg.Button('Mostrar Todas Bandeiras')],
                            [sg.Button('Voltar para Registro')]
        ]

        operacoesVeiculoLayout = [
                            [sg.Text('Escolha uma operação para fazer:')],
                            [sg.Button('Criar/Atualizar Veículo')],
                            [sg.Button('Deletar Veículo')],
                            [sg.Button('Mostrar Veículo')],
                            [sg.Button('Mostrar Todos Veículos')],
                            [sg.Button('Voltar para Registro')]
        ]

        operacoesCombustivelLayout = [
                            [sg.Text('Escolha uma operação para fazer:')],
                            [sg.Button('Criar/Atualizar Combustível')],
                            [sg.Button('Deletar Combustível')],
                            [sg.Button('Mostrar Combustível')],
                            [sg.Button('Mostrar Todos Combustíveis')],
                            [sg.Button('Voltar para Registro')]
        ]

        operacoesRegiaoLayout = [
                            [sg.Text('Escolha uma operação para fazer:')],
                            [sg.Button('Criar/Atualizar Região')],
                            [sg.Button('Deletar Região')],
                            [sg.Button('Mostrar Região')],
                            [sg.Button('Mostrar Todas Regiões')],
                            [sg.Button('Voltar para Registro')]
        ]

        # layouts de crud
        registrarAtualizarFuncionarioCrudLayout = [
                            [sg.Text("Digite as informações respectivas do funcionário:")],
                            [sg.Text('Nome:'),sg.InputText('', key='Nome')],
                            [sg.Text('Matrícula:'), sg.InputText('', key='Matricula')],
                            [sg.Text('CPF:'), sg.InputText('', key='CPF')],
                            [sg.Text('Data de Nascimento:'), sg.InputText('', key='Data Nascimento')],
                            [sg.Frame('', toolbar_buttons_regis_funcionario_crud)]
                          ]

        registrarAtualizarClienteConfirmacaoCrudLayout = [
                            [sg.Text("Deseja registrar um novo cliente?")],
                            [sg.Frame('', toolbar_buttons_register_cliente_confirmacao_crud)]
                        ]

        registrarAtualizarPessoaFisicaCrudLayout = [
                            [sg.Text("Digite as informações respectivas do cliente:")],
                            [sg.Text('Nome:'),sg.InputText('', key='Nome')],
                            [sg.Text('CPF:'), sg.InputText('', key='CPF')],
                            [sg.Text('RG:'), sg.InputText('', key='RG')],
                            [sg.Text('Data de Nascimento:'), sg.InputText('', key='Data Nascimento')],
                            [sg.Frame('', toolbar_buttons_regis_cliente_crud)]
                          ]

        registrarAtualizarPessoaJuridicaCrudLayout = [
                            [sg.Text("Digite as informações respectivas do cliente:")],
                            [sg.Text('Nome:'),sg.InputText('', key='Nome')],
                            [sg.Text('CNPJ:'), sg.InputText('', key='CNPJ')],
                            [sg.Text('Razão Social:'), sg.InputText('', key='Razao Social')],
                            [sg.Text('Tipo de Organização:'), sg.InputText('', key='Tipo Organizacao')],
                            [sg.Frame('', toolbar_buttons_regis_cliente_crud)]
                          ]

        registrarAtualizarBandeiraCrudLayout = [
                            [sg.Text("Digite as informações respectivas do bandeira:")],
                            [sg.Text('Nome:'),sg.InputText('', key='Nome')],
                            [sg.Text('URL:'), sg.InputText('', key='URL')],
                            [sg.Frame('', toolbar_buttons_regis_bandeira_crud)]
                          ]

        registrarAtualizarVeiculoCrudLayout = [
                            [sg.Text("Digite as informações respectivas do veículo:")],
                            [sg.Text('CPF do Cliente:'), sg.InputText('', key='CPF Cliente')],
                            [sg.Text('Placa Antiga:'),sg.InputText('', key='Placa Antiga')],
                            [sg.Text('Placa:'),sg.InputText('', key='Placa')],
                            [sg.Text('Marca:'), sg.InputText('', key='Marca')],
                            [sg.Text('Modelo:'), sg.InputText('', key='Modelo')],
                            [sg.Text('Ano:'), sg.InputText('', key='Ano')],
                            [sg.Frame('', toolbar_buttons_regis_veiculo_crud)]
                          ]

        registrarAtualizarCombustivelCrudLayout = [
                            [sg.Text("Digite as informações respectivas do combustível:")],
                            [sg.Text('Nome:'),sg.InputText('', key='Nome')],
                            [sg.Text('Preço:'), sg.InputText('', key='Preco')],
                            [sg.Frame('', toolbar_buttons_regis_combustivel_crud)]
                          ]

        registrarAtualizarRegiaoCrudLayout = [
                            [sg.Text("Digite as informações respectivas da região:")],
                            [sg.Text('Logradouro:'),sg.InputText('', key='Logradouro')],
                            [sg.Text('Número:'), sg.InputText('', key='Numero')],
                            [sg.Text('Complemento:'), sg.InputText('', key='Complemento')],
                            [sg.Text('Bairro:'), sg.InputText('', key='Bairro')],
                            [sg.Text('Cidade:'), sg.InputText('', key='Cidade')],
                            [sg.Text('Estado:'), sg.InputText('', key='Estado')],
                            [sg.Text('País:'), sg.InputText('', key='Pais')],
                            [sg.Frame('', toolbar_buttons_regis_regiao_crud)]
                          ]

        # layouts de abastecimento
        abastecerLayout = [
                            [sg.Text("Escolha uma das opções abaixo:")],
                            [sg.Text('Matricula:'),sg.InputText('', key='Matricula')],
                            [sg.Text('Veiculo:'), sg.InputText('', key='Veiculo')],
                            [sg.Text('Cliente:'), sg.InputText('', key='Cliente')],
                            [sg.Text('Combustivel:'), sg.Text('', key='Combustivel')],
                            [sg.Text('Preço:'), sg.Text('', key='Preco')],
                            [sg.Text('Quantidade (l):'), sg.InputText('', key='Quantidade')],
                            [sg.Text('Subtotal:'), sg.Text('', key='SubTotal')],
                            [sg.Frame('', toolbar_buttons_abs)]
                          ]

        registrarPessoaFisicaLayout = [
                            [sg.Text("Digite as informações respectivas do cliente:")],
                            [sg.Text('Nome:'),sg.InputText('', key='Nome')],
                            [sg.Text('CPF:'), sg.InputText('', key='CPF')],
                            [sg.Text('RG:'), sg.InputText('', key='RG')],
                            [sg.Text('Data de Nascimento:'), sg.InputText('', key='Data Nascimento')],
                            [sg.Frame('', toolbar_buttons_regis_cliente)]
                          ]

        registrarPessoaJuridicaLayout = [
                            [sg.Text("Digite as informações respectivas do cliente:")],
                            [sg.Text('Nome:'),sg.InputText('', key='Nome')],
                            [sg.Text('CNPJ:'), sg.InputText('', key='CNPJ')],
                            [sg.Text('Razão Social:'), sg.InputText('', key='Razao Social')],
                            [sg.Text('Tipo de Organização:'), sg.InputText('', key='Tipo Organizacao')],
                            [sg.Frame('', toolbar_buttons_regis_cliente)]
                          ]

        registrarVeiculoLayout = [
                            [sg.Text("Digite as informações do veículo:")],
                            [sg.Text('CPF do Cliente:'), sg.InputText('', key='CPF Cliente')],
                            [sg.Text('Placa Antiga:'),sg.InputText('', key='Placa')],
                            [sg.Text('Placa:'),sg.InputText('', key='Placa')],
                            [sg.Text('Marca:'), sg.InputText('', key='Marca')],
                            [sg.Text('Modelo:'), sg.InputText('', key='Modelo')],
                            [sg.Text('Ano:'), sg.InputText('', key='Ano')],
                            [sg.Frame('', toolbar_buttons_abs_veiculo)]
                          ]


        deletarFuncionarioLayout = [
                            [sg.Text("Digite a matrícula do funcionário a ser removido:")],
                            [sg.Text('Matrícula:'), sg.InputText('', key='Matricula')],
                            [sg.Frame('', toolbar_buttons_abs_deletar_funcionario)]
                          ]

        verRegistrosLayout = [
                            [sg.Text("Digite o nome do registro:")],
                            [sg.Text('Tabela:'), sg.InputText('', key='Tabela')],
                            [sg.Frame('', toolbar_buttons_abs_ver_registros)]
                          ]

        registrarClienteConfirmacaoLayout = [
                            [sg.Text("Cliente não existe no sistema.\nDeseja registrar um novo cliente?")],
                            [sg.Frame('', toolbar_buttons_register)]
                         ]

        registrarVeiculoConfirmacaoLayout = [
                            [sg.Text("Esse veículo não existe no sistema.\nDeseja criar um novo registro?")],
                            [sg.Frame('', toolbar_buttons_register_veiculo)]
                         ]

        funcionarioInexistenteLayout = [
                            [sg.Text("O número de matrícula do funcionário está incorreto")],
                            [sg.Frame('', toolbar_buttons_regis_funcionario)]
                         ]

        registroLayout = [
                            [sg.Text("Cadastre conforme é pedido:")],
                            [sg.Frame('', toolbar_buttons_regis)]
                         ]

        abastecidoLayout = [
                            [sg.Text("O carro foi abastecido.")],
                            [sg.Frame('', toolbar_buttons_regis)]
                         ]
# nesta tupla ficará todos os combustiveis + preços
        combustiveis = operacoes.selectAllCombustivel()
        names = []
        for combustivel in combustiveis:
            names.append([combustivel['nome'], str(combustivel['preco']), str(combustivel['id_combustivel'])])
        tableLayout = [
            [sg.Table(values=names,
                      enable_events=False,
                      display_row_numbers=True,
                      headings=['Combustivel', 'Preço', 'Id'],
                      key='_table_',
                      select_mode=True)],
            [sg.Frame('', toolbar_buttons_popup)]
        ]

# Windows
        self.window = sg.Window('Posto LAR', size=(300, 300)).Layout(layout)

# Read Window
        x = 0
        while True:

            button, value = self.window.Read()
            print(value)
            try:
                print()
            finally:

                if button == 'Registro':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', location=(width, height), size=(400, 400)).Layout(cadastrosLayout)

                if x == 1:
                    self.window.Element('Combustivel').Update(combustivell)
                    self.window.Element('Preco').Update(preco)
                    x = 0

                if button == 'Abastecer':
                    self.window.Close()

                    self.window_popup= sg.Window("Escolha o combustivel", size=(400, 400)).Layout(tableLayout)
                    button_popup,value_popup = self.window_popup.Read()

                    if button_popup == 'Ok':
                        combustivel = names[value_popup['_table_'][0]]
                        preco = combustivel[1]
                        combustivell = combustivel[0]
                        self.window_popup.Close()

                    self.window = sg.Window('Posto LAR', size=(400, 400)).Layout(abastecerLayout)
                    x = 1
                
                elif button == 'Voltar':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(400, 400)).Layout(layout)

                elif button == 'Calcular':
                    novoPreco = float(value['Quantidade']) * float(combustivel[1])
                    self.window.Element('SubTotal').Update(novoPreco)

                elif button == 'Finalizar':
                    novoPreco = float(value['Quantidade']) * float(combustivel[1])
                    abastecimentoResult = self.endAbastecimento(value['Cliente'], value['Matricula'], value['Veiculo'], combustivel[2], novoPreco)
                    if abastecimentoResult == 0:
                        self.window.Close()
                        self.window = sg.Window('Posto LAR', size=(400, 400)).Layout(abastecidoLayout)
                    elif abastecimentoResult == 1:
                        self.window.Close()
                        self.window = sg.Window('Posto LAR', size=(320, 50)).Layout(funcionarioInexistenteLayout)
                    elif abastecimentoResult == 2:
                        self.window.Close()
                        self.window = sg.Window('Posto LAR', size=(400, 400)).Layout(registrarClienteConfirmacaoLayout)
                    elif abastecimentoResult == 3:
                        self.window.Close()
                        self.window = sg.Window('Posto LAR', size=(400, 400)).Layout(registrarVeiculoConfirmacaoLayout)

                elif button == 'Pessoa Física':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(400, 400)).Layout(registrarPessoaFisicaLayout)

                elif button == 'Pessoa Jurídica':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(400, 400)).Layout(registrarPessoaJuridicaLayout)

                elif button == 'Registrar Cliente':
                    self.registerCliente(value)
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(400, 400)).Layout(abastecerLayout)

                elif button == 'Novo Veículo':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(400, 400)).Layout(registrarVeiculoLayout)

                elif button == 'Tentar Novamente':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(400, 400)).Layout(abastecerLayout)

                elif button == 'Cancelar':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(300, 300)).Layout(layout)

                elif button == 'Adicionar':
                    self.registerVeiculo(value)
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(400, 400)).Layout(abastecerLayout)

                elif button == 'Modificar':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(400, 400)).Layout(abastecerLayout)

                elif button is None or button == 'Close' or button == 'Sair':
                    self.window.Close()
                    break

                elif button == 'Ok' or button == 'Voltar':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(300, 300)).Layout(layout)

                elif button == 'Confirmar':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(300, 300)).Layout(layout)

                elif button == 'Voltar para Registro':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(400, 400)).Layout(cadastrosLayout)

                #crud do bd
                elif button == 'Funcionario':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(500, 500)).Layout(operacoesFuncionarioLayout)

                elif button == 'Cliente':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(500, 500)).Layout(operacoesClienteLayout)

                elif button == 'Bandeira':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(500, 500)).Layout(operacoesBandeiraLayout)

                elif button == 'Veículo':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(500, 500)).Layout(operacoesVeiculoLayout)

                elif button == 'Combustível':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(500, 500)).Layout(operacoesCombustivelLayout)

                elif button == 'Região':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(500, 500)).Layout(operacoesRegiaoLayout)

                elif button == 'Criar/Atualizar Funcionário':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(500, 500)).Layout(registrarAtualizarFuncionarioCrudLayout)

                elif button == 'Criar/Atualizar Cliente':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(600, 600)).Layout(registrarAtualizarClienteConfirmacaoCrudLayout)
                    
                elif button == 'Criar/Atualizar Pessoa Física':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(600, 600)).Layout(registrarAtualizarPessoaFisicaCrudLayout)

                elif button == 'Criar/Atualizar Pessoa Jurídica':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(600, 600)).Layout(registrarAtualizarPessoaJuridicaCrudLayout)

                elif button == 'Criar/Atualizar Bandeira':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(500, 500)).Layout(registrarAtualizarBandeiraCrudLayout)
                    
                elif button == 'Criar/Atualizar Veículo':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(500, 500)).Layout(registrarAtualizarVeiculoCrudLayout)
                    
                elif button == 'Criar/Atualizar Combustível':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(500, 500)).Layout(registrarAtualizarCombustivelCrudLayout)

                elif button == 'Criar/Atualizar Região':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(500, 500)).Layout(registrarAtualizarRegiaoCrudLayout)
                    
                elif button == 'Atualizar Veículo':
                    self.updateVeiculo(value)
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(500, 500)).Layout(cadastrosLayout)

                elif button == 'Deletar Funcionário':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(500, 500)).Layout(deletarFuncionarioLayout)

                elif button == 'Deletar Registro do Funcionário':
                    operacoes.deleteFuncionario(value['Matricula'])
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(500, 500)).Layout(cadastrosLayout)

                elif button == 'Ver Registros':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(500, 500)).Layout(verRegistrosLayout)

                elif button == 'Mostrar Registros':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(500, 500)).Layout(registrosLayout)

                elif button == 'Voltar para Início':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', size=(300, 300)).Layout(layout)

    def endAbastecimento(self, cpfCnpj, matricula, placa, idCombustivel, precoFinal):
        posto_cnpj = operacoes.selectAllPosto()
        cliente = self.checkIfClienteExists(cpfCnpj)
        funcionario = self.checkFuncionarioMatricula(matricula)
        veiculo = self.checkIfVeiculoExists(placa)
        if cliente and funcionario and veiculo:
            operacoes.createAbastecimento(posto_cnpj[0]['cnpj_posto'], matricula, placa)
            operacoes.createAbastecimentoCombustivel(idCombustivel, precoFinal)
        if not funcionario:
            return 1
        if not cliente:
            return 2
        if not veiculo:
            return 3
        return 0

    def checkIfClienteExists(self, cpfCnpj):
        cliente = operacoes.selectClienteByCpfCnpj(cpfCnpj)
        if not cliente:
            return None
        else:
            return cliente

    def checkFuncionarioMatricula(self, matricula):
        funcionario = operacoes.selectFuncionarioByMatricula(matricula)
        if not funcionario:
            return None
        else:
            return funcionario

    def checkIfVeiculoExists(self, placa):
        veiculo = operacoes.selectVeiculoByPlaca(placa)
        if not veiculo:
            return None
        else:
            return veiculo

    def registerCliente(self, data):
        resultCliente = operacoes.createCliente(data['Nome'])
        print("resultado id: " + str(resultCliente))
        if 'CPF' in data:
            resultPessoaFisica = operacoes.createPessoaFisica(resultCliente, data['CPF'], data['RG'], data['Data Nascimento'])
        else:
            resultPessoaJuridica = operacoes.createPessoaJuridica(resultCliente, data['Razao Social'], data['CNPJ'], data['Tipo Organizacao'])

    def registerVeiculo(self, data):
        codCliente = operacoes.selectClienteByCpfCnpj(data['CPF Cliente'])
        result = operacoes.createVeiculo(data['Placa'], codCliente[0]['cod_cliente'], data['Marca'], data['Modelo'], data['Ano'])

    def updateVeiculo(self, data):
        operacoes.updateVeiculo(data['Placa'], data['Marca'], data['Modelo'], data['Ano'], data['Placa Antiga'])

    def deleteFuncionario(self, matricula):
        operacoes.deleteFuncionario(matricula)

teste = Gui()
teste.show()