#from negocio import operacoes

import PySimpleGUIQt as sg
import os

class Gui:
    def __init__(self):
        self.BUTTON_PATH = '.'
        self.button_names_main = ('Abastecer', 'Registro', 'Close')
        self.button_names_abs = ('Voltar','Calcular','Finalizar')
        self.button_names_regis = ()
        self.window = None

    # toolbar_buttons
    def configToobarBtn(self, lista_btn):

        button_files = [os.path.join(self.BUTTON_PATH, b + '.png') for b in lista_btn]

        toolbar_buttons = [[sg.RButton('{}'.format(lista_btn[i]), image_size=(32, 32), pad=(0, 0),
                                       tooltip=lista_btn[i]) for i, f in enumerate(button_files)], ]
        return toolbar_buttons

    def show(self):

        sg.SetOptions(auto_size_buttons=True, margins=(0, 0), button_color=sg.COLOR_SYSTEM_DEFAULT)

        toolbar_buttons_init    = self.configToobarBtn(self.button_names_main)
        toolbar_buttons_abs     = self.configToobarBtn(self.button_names_abs)
        toolbar_buttons_regis   = self.configToobarBtn(self.button_names_regis)

# Layout
        layout = [
                    [sg.Text("Escolha uma das opções abaixo")],
                    [sg.Frame('', toolbar_buttons_init)]
                 ]

        # chamar do banco o combustivel e preço
        preco = str(3.84)
        combustivel = 'Gasolina'

        abastecerLayout = [
                            [sg.Text("Escolha uma das opções abaixo:")],
                            [sg.Text('Matricula:'),sg.InputText('', key='Matricula')],
                            [sg.Text('Veiculo:'), sg.InputText('', key='Veiculo')],
                            [sg.Text('Cliente:'), sg.InputText('', key='Cliente')],
                            [sg.Text('Combustivel:'), sg.Text(text=combustivel, key='Combustivel')],
                            [sg.Text('Preço:'), sg.Text(text=preco, key='Preco')],
                            [sg.Text('Quantidade:'), sg.InputText('', key='Quantidade')],
                            [sg.Text('Subtotal:'), sg.Text('', key='SubTotal')],
                            [sg.Frame('', toolbar_buttons_abs)],
                          ]

        registroLayout = [
                            [sg.Text("Cadastre conforme é pedido:")],
                            [sg.Frame('', toolbar_buttons_regis)]
                         ]

# Windows
        self.window = sg.Window('Posto LAR', location=(600, 450), size=(400, 400)).Layout(layout)

# Read Window
        while True:

            button, value = self.window.Read()
            try:

                print("")
            except:
                print("here")
            finally:

                if button == 'Registro':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', location=(600, 450), size=(400, 400)).Layout(registroLayout)

                elif button == 'Abastecer':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', location=(600, 450), size=(400, 400)).Layout(abastecerLayout)

                elif button == 'Voltar':
                    self.window.Close()
                    self.window = sg.Window('Posto LAR', location=(600, 450), size=(400, 400)).Layout(layout)

                elif button == 'Calcular':
                    novoPreco = float(value['Quantidade']) * float(preco)
                    self.window.Element('SubTotal').Update(novoPreco)


                elif button == 'Finalizar':

                    print("Aqui")

                elif button == 'Close':
                    self.window.Close()
                    break

                else:
                    self.window.Close()
                    break

teste = Gui()
teste.show()