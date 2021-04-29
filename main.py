# pip install bs4
# pip install requests
from bs4 import BeautifulSoup
import requests
import PySimpleGUI as sg

# inseringo interface grafica com PysimpleGUI

campos = [
    [sg.Text('Escreva o nome da cidade')],
    [sg.Text('Ex: "Rio de janeio, Paris, Moscow"')],
    [sg.Input(key='local')],
    [sg.Output(key='resultado')],
    [sg.Button('Buscar'), sg.Button('Fechar'), sg.Button('Limpar')]
]
# Criando Janela
janela = sg.Window('Informação do Clima', campos)


def temperatura(valor):
    # Faz uma busca no google e obtem a temperatura da cidade informada
    pesquisa = valores['local']
    url = f'https://www.google.com/search?q=clima+{pesquisa}'
    r = requests.get(url)
    s = BeautifulSoup(r.text, 'html.parser')
    info = s.find('div', class_='BNeawe').text
    return info


while True:
    # faz a leitura do layout
    eventos, valores = janela.read()
    try:
        # Encerra aplicação
        if eventos == sg.WINDOW_CLOSED or eventos == 'Fechar':
            break
        # Mostra na tela Resultado
        elif eventos == 'Buscar' and valores['local'] != "":
            print(temperatura(valores))
        # Limpa os Campos
        elif eventos == 'Limpar':
            janela['local'].update('')
            janela['resultado'].update('')
            valores['local'] = ""

    except:
        print('Operação invalida')
        print('Erro: Verifique se digitou a cidade corretamente')
