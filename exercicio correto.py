from time import sleep
def grava_arquivo(cotacao):
    with open('cotacao_dolar.txt','a') as arquivo_cotacao:
        arquivo_cotacao.write(str(cotacao) + "\n")

for i in range(10):
    print(i)
    grava_arquivo(str(i))
    sleep(5)
