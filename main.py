import pandas as pd
from twilio.rest import Client

#É necessário cria uma conta no Twilio
#https://www.twilio.com/docs/libraries/python

#CONFIGURAÇÕES DO TWILIO PARA ENVIO DO SMS

# Your Account SID from twilio.com/console
account_sid = "XXXXXXXXXXXXXXXXXXXXXXXX" #colocar  a conta aqui
# Your Auth Token from twilio.com/console
auth_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" #colocar o token aqui
client = Client(account_sid, auth_token)


#passo a passo de solução

#abrir os 6 arquivos em excel
#criando uma lista para armazenar
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

#para cada mês dentro da lista_meses,imprimir o mes e ler o arquivo excel
for mes in lista_meses:
    #abrindo os arquivos  excel, mas usando a lista: é necessário colocar os arquivos na mesma pasta do código python
    #f serve para formatar a string
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    #para cada  arquivo:
    #Verificar se algum valor na coluna Vendas  daquele arquivo é maior que 55.000
    #Se algum valor da coluna vendas for maior do que 55.000 -> Envia sms, com nome, mes e as vendas dele
    if (tabela_vendas['Vendas'] > 55000).any():
        # capturando o registro que vendeu mais
        #o método "loc", tem dois parametros: linha e coluna. A linha é a própria condição. Só que o loc retorna uma tabela. é necessário pegar o valor com o values
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,"Vendedor"].values[0]
        valor =tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,"Vendas"].values[0]
        #enviar sms
        message = client.messages.create(
            to="+5511xxxxxxxxx", #coloque o numero do celuaklr que receberá a mensaagem. para conta gratuita no Twilio usar seu núemrop cadastrado
            from_="+15XXXXXXX", #Coloque seu número cadastrado aqui
            body=f'No mês {mes} Alguém bateu a meta. O vendedor {vendedor} bateu a meta com {valor}')
        print(message.sid)

# Caso não seja maior que 55 mil, não fazer nada

#Necessário que instalar os módulos necessários para enviar sms, abri excel etc.. -------------

# para instalar no terminal do python: #pip install

#pandas : para analise de dados
#openpyxls: para manipular arquivo excel
#twilio: para enviar mensagens sms




