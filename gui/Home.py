import PySimpleGUIQt as sg
import os

class Gui:
    def __init__(self):
        self.BUTTON_PATH = '.'
        self.button_names = ('Create', 'Remove', 'Update', 'Delete', 'Close')
        self.window = None

    def show(self):
        button_files = [os.path.join(self.BUTTON_PATH, b + '.png') for b in self.button_names]

        sg.SetOptions(auto_size_buttons=True, margins=(0, 0), button_color=sg.COLOR_SYSTEM_DEFAULT)

        toolbar_buttons = [[sg.RButton('{}'.format(self.button_names[i]), image_size=(32, 32), pad=(0, 0),
                                       tooltip=self.button_names[i]) for i, f in enumerate(button_files)], ]

        names = [['lucas', '23'], ['rodrigo', '26'], ['andre', '25'], ['emerson', '13'], ['ericka', '21']]
        layout = [[sg.Table(values=names, headings=['Name', 'Idade'], num_rows=len(names), select_mode=True)],
                  [sg.Frame('', toolbar_buttons)]]

        self.window = sg.Window('Window Title', location=(800, 600)).Layout(layout)

        while True:

            button, value = self.window.Read()
            if button == 'Close' or button is None:
                self.window.Close()
                break  # exit button clicked
            elif button == 'Create':
                answer = sg.PopupYesNo('Are you sure?')
                print(answer)

                if answer == 'Yes':
                    sg.PopupError("Opps! something it's wrong")
            else:
                print(button)

teste = Gui()
teste.show()
