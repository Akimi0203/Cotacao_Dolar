import time
import pyautogui
import requests
import json
import time

cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
# print(cotacao)
cotacao = cotacao.json()
cotacao_dolar = cotacao['USDBRL']['bid']

cotacao_dolaraAsk = cotacao['USDBRL']['ask']

cotacao_dolarVarBid = cotacao['USDBRL']['varBid']

cotacao_dolarPct = cotacao['USDBRL']['pctChange']

cotacao_dolarHigh = cotacao['USDBRL']['high']

cotacao_dolarLow = cotacao['USDBRL']['low']

cotacao_dolarTimestamp = cotacao['USDBRL']['timestamp']

cotacao_dolarCreate_date = cotacao['USDBRL']['create_date']

arquivo = open("Legendas.txt", "a")
dec = 0
if dec == 0:
    while dec == 0:
        arquivo.write(f"{cotacao_dolar}; {cotacao_dolaraAsk};{cotacao_dolarVarBid};{cotacao_dolarPct};{cotacao_dolarHigh};{cotacao_dolarLow};{cotacao_dolarTimestamp};{cotacao_dolarCreate_date} \n")
        print("Rodando...")
        time.sleep(30)
        reset = pyautogui.hotkey("shift", "f10")
        pyautogui.typewrite(reset)





