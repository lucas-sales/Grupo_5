from negocio import operacoes
import PySimpleGUIQt as sg
import os

class Gui:
    def __init__(self):
        self.BUTTON_PATH = '.'
        self.button_names_main = ('Abastecer', 'Registro', 'Close')
        self.button_names_abs = ('Voltar','Calcular','Finalizar')
        self.button_names_regis = ('Ok', 'Cancelar')
        self.window = None
        self.window_popup = None

    # toolbar_buttons
    def configToobarBtn(self, lista_btn):

        button_files = [os.path.join(self.BUTTON_PATH, b + '.png') for b in lista_btn]

        toolbar_buttons = [[sg.RButton('{}'.format(lista_btn[i]), image_size=(32, 32), pad=(0, 0),
                                       tooltip=lista_btn[i]) for i, f in enumerate(button_files)], ]
        return toolbar_buttons

    def show(self):
        width = 1500
        height = 150

        sg.SetOptions(auto_size_buttons=True, margins=(0, 0), button_color=sg.COLOR_SYSTEM_DEFAULT)

        toolbar_buttons_init    = self.configToobarBtn(self.button_names_main)
        toolbar_buttons_abs     = self.configToobarBtn(self.button_names_abs)
        toolbar_buttons_regis   = self.configToobarBtn(self.button_names_regis)
        toolbar_buttons_popup   = self.configToobarBtn(self.button_names_regis)

# Layout
        layout = [
                    [sg.Text("Escolha uma das opções abaixo")],
                    [sg.Frame('', toolbar_buttons_init)]
                 ]

        preco = None
        combustivell = None

        cadastrosLayout = [
                            [sg.Text('Escolha o que deseja cadastrar:')],
                            [sg.Button('Funcionario')],
                            [sg.Button('Combustível')],
                            [sg.Button('Bandeira')],
                            [sg.Button('Veículo')],
                            [sg.Button('Região')],
                            [sg.Text('')],
                            [sg.Button('Confirmar'), sg.Button('Sair')]
        ]

        abastecerLayout = [
                            [sg.Text("Escolha uma das opções abaixo:")],
                            [sg.Text('Matricula:'),sg.InputText('', key='Matricula')],
                            [sg.Text('Veiculo:'), sg.InputText('', key='Veiculo')],
                            [sg.Text('Cliente:'), sg.InputText('', key='Cliente')],
                            [sg.Text('Combustivel:'), sg.Text('', key='Combustivel')],
                            [sg.Text('Preço:'), sg.Text('', key='Preco')],
                            [sg.Text('Quantidade:'), sg.InputText('', key='Quantidade')],
                            [sg.Text('Subtotal:'), sg.Text('', key='SubTotal')],
                            [sg.Frame('', toolbar_buttons_abs)],
                          ]

        registroLayout = [
                            [sg.Text("Cadastre conforme é pedido:")],
                            [sg.Frame('', toolbar_buttons_regis)]
                         ]
# nesta tupla ficará todos os combustiveis + preços
        combustiveis = operacoes.selectAllCombustivel()
        names = []
        for combustivel in combustiveis:
            names.append([combustivel['nome'], str(combustivel['preco'])])
        tableLayout = [
            [sg.Table(values=names,
                      enable_events=False,
                      display_row_numbers=True,
                      headings=['Combustivel', 'Preço'],
                      key='_table_',
                      select_mode=True)],
            [sg.Frame('', toolbar_buttons_popup)]
        ]

# Windows
        self.window = sg.Window('Posto LAR', size=(400, 400)).Layout(layout)

# Read Window
        x = 0
        while True:

            button, value = self.window.Read()
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

                    self.window_popup= sg.Window("Escolha o combustivel",location=(width, height), size=(400, 400)).Layout(tableLayout)
                    button_popup,value_popup = self.window_popup.Read()

                    if button_popup == 'Ok':
                        combustivel = names[value_popup['_table_'][0]]
                        preco = combustivel[1]
                        combustivell = combustivel[0]
                        self.window_popup.Close()

                    self.window = sg.Window('Posto LAR', location=(width, height), size=(400, 400)).Layout(abastecerLayout)
                    x = 1
                
                elif button == 'Voltar':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', location=(width, height), size=(400, 400)).Layout(layout)

                elif button == 'Calcular':
                    novoPreco = float(value['Quantidade']) * float(combustivel[1])
                    self.window.Element('SubTotal').Update(novoPreco)

                elif button == 'Finalizar':

                    print("Aqui")

                elif button is None or button == 'Close':
                    self.window.Close()
                    break

teste = Gui()
teste.show()