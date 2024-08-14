import openpyxl 
from urllib.parse import quote
import webbrowser
import pyautogui as gui
import os
from time import sleep

webbrowser.open('https://web.whatsapp.com/')
sleep(20)  


clientes = openpyxl.load_workbook('Exemplo.xlsx')
pagina_clientes = clientes['Planilha1']


for linha in pagina_clientes.iter_rows(min_row=2):
    nome = linha[2].value
    telefone = linha[3].value

    if nome is None or telefone is None:
        continue  

    mensagem = f'Olá {nome}! Esta é uma mensagem automatizada em Python.'

    try:
        
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone=55{telefone}&text={quote(mensagem)}'
        webbrowser.open(link_mensagem_whatsapp)
        sleep(20) 
        try:
            seta = gui.locateCenterOnScreen('seta.jpg')
            if seta:
                sleep(5)
                gui.click(seta[0], seta[1])
            else:
                print(f'Imagem da seta não encontrada para {nome}, usando coordenadas fixas.')
                
                gui.click(1000, 750)  
        except Exception as e:
            print(f'Erro ao localizar/clicar na seta para {nome}: {str(e)}')

        sleep(5)
        gui.hotkey('ctrl', 'w')
        sleep(5)
    except Exception as e:
        print(f'Não foi possível enviar mensagem para {nome}: {str(e)}')
        with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone}{os.linesep}')