#from negocio import operacoes

import PySimpleGUIQt as sg
import os

class Gui:
    def __init__(self):
        self.BUTTON_PATH = '.'
        self.button_names_main = ('Abastecer', 'Registro', 'Close')
        self.button_names_abs = ('Matricula', 'Cliente', 'Veiculo','Combustivel', 'Preço', 'Subtotal', 'Voltar')
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

        abastecerLayout = [
                            [sg.Text("Escolha uma das opções abaixo")],
                            [sg.Frame('', toolbar_buttons_abs)]
                          ]

        registroLayout = [
                            [sg.Text("Cadastre conforme é pedido:")],
                            [sg.Frame('', toolbar_buttons_regis)]
                         ]

# Windows
        self.window = sg.Window('Posto LAR', location=(800, 600)).Layout(layout)

# Read Window
        while True:

            button, value = self.window.Read()
            if button == 'Registro':
                self.window.Close()
                self.window = sg.Window('Posto LAR', location=(800, 600)).Layout(registroLayout)

            elif button == 'Abastecer':
                self.window.Close()
                self.window = sg.Window('Posto LAR', location=(800, 600)).Layout(abastecerLayout)

            elif button == 'Matricula':
                print("Aqui")

            elif button == 'Cliente':
                print("Aqui")

            elif button == 'Veiculo':
                print("Aqui")

            elif button == 'Combustivel':
                print("Aqui")

            elif button == 'Preço':
                print("Aqui")

            elif button == 'SubTotal':
                print("Aqui")

            elif button == 'Voltar':
                self.window.Close()
                self.window = sg.Window('Posto LAR', location=(800, 600)).Layout(layout)

            elif button == 'Close':
                self.window.Close()
                break

            else:
                self.window.Close()
                break

teste = Gui()
teste.show()