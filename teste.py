from negocio import operacoes
import PySimpleGUIQt as sg
import os

width = 400
height = 400

layoutMain = [
              [sg.Text('Escolha a tabela para consulta:')],
              [sg.Text('')],
              [sg.Button('Funcionários', size=(100, 30)),
              sg.Button('Veículos', size=(100, 30)),
              sg.Button('Bandeiras', size=(100, 30)),
              sg.Button('Combustivel', size=(100, 30))],
              [sg.Text('')],
              [sg.Button('Sair')]
]

layoutConsulta = [
          [sg.Text('Consultas do BD')],
          [sg.Listbox([], key='listBox')],
          [sg.Button('Obter do BD'), sg.Button('Sair')]
          ]

window = sg.Window('Consulta do BD', size=(width, height)).Layout(layoutMain)

def getDicsAsListOfStrings(ListaDeChavesDoDicionario, listaDeDicionarios):
    result = []
    for dic in listaDeDicionarios:
        dicAsString = ''
        chave = 0
        while chave < len(ListaDeChavesDoDicionario):
            if chave == 0:
                dicAsString = str(dic[ListaDeChavesDoDicionario[chave]])
            elif chave == len(ListaDeChavesDoDicionario) - 1:
                dicAsString = dicAsString + ' - ' + str(dic[ListaDeChavesDoDicionario[chave]])
                result.append(dicAsString)
            else:
                dicAsString += ' - ' + str(dic[ListaDeChavesDoDicionario[chave]])
            chave = chave + 1
    return result

listBoxInput = None
while True:
    event, values = window.Read()
    print(event, values)

    if event is None or event == 'Sair':
        print('Ended by hit "close" or "Exit" button.')
        break
        
    elif event == 'Funcionários':
        window.Close()
        buscaBD = operacoes.selectAllFuncionario()
        listBoxInput = getDicsAsListOfStrings(['matricula', 'nome', 'data_nascimento', 'cpf'], buscaBD)
        window = sg.Window('Mostra Funcionários', size=(width, height)).Layout(layoutConsulta)
    
    elif event == 'Veículos':
        window.Close()
        buscaBD = operacoes.selectAllVeiculo()
        listBoxInput = getDicsAsListOfStrings(['placa', 'cod_cliente', 'marca', 'modelo', 'ano'], buscaBD)
        window = sg.Window('Mostra Veículos', size=(width, height)).Layout(layoutConsulta)

    elif event == 'Bandeiras':
        window.Close()
        buscaBD = operacoes.selectAllBandeira()
        listBoxInput = getDicsAsListOfStrings(['nome_bandeira', 'url'], buscaBD)
        window = sg.Window('Mostra Bandeiras', size=(width, height)).Layout(layoutConsulta)

    elif event == 'Combustivel':
        window.Close()
        buscaBD = operacoes.selectAllCombustivel()
        listBoxInput = getDicsAsListOfStrings(['id_combustivel', 'nome', 'preco'], buscaBD)
        window = sg.Window('Mostra Combustíveis', size=(width, height)).Layout(layoutConsulta)

    elif event == 'Obter do BD':
        window.Element('listBox').Update(listBoxInput)

window.Close()