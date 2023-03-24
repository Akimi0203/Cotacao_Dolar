import datetime
from time import sleep
import requests
import json
import datetime #para pegar a hr local

def grava_arquivo(cotacao):
    with open('cotacao_dolar.txt','a') as arquivo_cotacao:
        arquivo_cotacao.write(str(cotacao) + "\n")

with open('cotacao_dolar.txt','a') as arquivo_cotacao:
    arquivo_cotacao.write('Compra; Venda; Maior Valor; Menor Valor; Variacao; Time Stamp; Data e Hora'+"\n")

for i in range(50):
    print(i)
    cotacao = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL")
    cotacao = cotacao.json()
    cotacao_dolar = cotacao['BTCBRL']['bid']
    #cotacao dolar passa a ser tudo que ele já tinha, mais o que ele acrescentou.

    cotacao_dolar = cotacao_dolar + ";" + cotacao['BTCBRL']['ask']
    cotacao_dolar = cotacao_dolar + ";" + cotacao['BTCBRL']['high']
    cotacao_dolar = cotacao_dolar + ";" + cotacao['BTCBRL']['low']
    cotacao_dolar = cotacao_dolar + ";" + cotacao['BTCBRL']['varBid']
    cotacao_dolar = cotacao_dolar + ";" + cotacao['BTCBRL']['timestamp']
    cotacao_dolar = cotacao_dolar + ";" + cotacao['BTCBRL']['create_date']

    hora_local = datetime.datetime.now()
    cotacao_dolar = cotacao_dolar + ";" + str(hora_local)

    grava_arquivo(str(cotacao_dolar))
    print(cotacao_dolar)

    #30(menos repetição)
    sleep(5)
