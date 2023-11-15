import requests
from tkinter import *

def obter_cidade(event=None):
    num_digitado = entrada.get()
    try:
        numero = int(num_digitado)
        janela.after(200, limpar_mensagem)
        return(numero)    
    except ValueError:
        label_resultado.config(text="Por favor, digite um número válido.")

def limpar_mensagem():
    label_resultado.config(text="")

def cidadealbion():    
    url = requests.get("https://west.albion-online-data.com/api/v2/stats/Prices/T4_2H_CLEAVER_HELL%401.json")

    informacoes = url.json()

    item = informacoes[0]['item_id']
    if item == 'T4_2H_CLEAVER_HELL@1':
        item = 'T4 Carving Sword'
    a = obter_cidade()
    cidade = informacoes[a]['city']

    item_resp['text'] = f'{item}'
    cidade_resp['text'] = f'{cidade}'


janela = Tk()

janela.title('Cidade Albion')
texto_entrada = Label(janela, text='Digite o numero da cidade que deseja\n 10 - Bridgewatch \n 15 - Caerleon \n 20 - Fort Sterling \n 25 - Lymhurst \n 30 - Martlock \n 35 - Thetford \n 2 - Black Market')
texto_entrada.grid(column=0, row=0)
entrada = Entry(janela, width=3)
entrada.grid(column=0, row=1)
entrada.bind('<Return>', obter_cidade)
label_resultado = Label(janela, text="")
label_resultado.grid(column=0, row=2)

botao = Button(janela, text='Gerar Cidade e item', command=cidadealbion)
botao.grid(column=0, row=3)

texto_item = Label(janela, text=f'ITEM')
texto_item.grid(column=0, row=4)
item_resp = Label(janela, text=f'')
item_resp.grid(column=0, row=5)

texto_cidade = Label(janela, text=f'CIDADE')
texto_cidade.grid(column=0, row=6)
cidade_resp = Label(janela, text=f'')
cidade_resp.grid(column=0, row=7)

janela.mainloop()