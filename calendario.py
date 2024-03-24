from apscheduler.schedulers.blocking import BlockingScheduler
import tweepy
import re
from datetime import datetime
from oponente import oponente
from info_jogo import competicao, dia, hora
from config import consumer_key, consumer_secret, bearer_token, access_token, access_token_secret

# Você pode reproduzir a execução em outra conta criando um arquivo config.py e inserindo suas chaves do Twitter Developer Portal

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def calcular_dias(data_jogo):
    hoje = datetime.now()
    data_jogo = datetime.strptime(data_jogo, "%Y-%m-%d")
    dias_faltando = (data_jogo - hoje).days
    return dias_faltando + 1

def postar_tweet():
    if isinstance(dia, re.Match):
        dia = dia.group()

    if isinstance(competicao, re.Match):
        competicao = competicao.group()

    match = re.search(r'\d{4}-\d{2}-\d{2}', dia)
    if match:
        dia = match.group()

    dias_faltando = calcular_dias(dia)

    if competicao == "Amistosos":
        if dias_faltando > 1:
            client.create_tweet(text=f"Faltam {dias_faltando} dias para o Vasco entrar em campo contra o(a) {oponente} em um jogo amistoso.")
        elif dias_faltando == 1:
            client.create_tweet(text=f"Falta {dias_faltando} dia para o Vasco entrar em campo contra o(a) {oponente} em um jogo amistoso.")
        else:
            client.create_tweet(text=f"Hoje tem Vasco! O Gigante entra em campo contra o(a) {oponente} em um jogo amistoso às {hora}.")
    else:
        if dias_faltando > 1:
            client.create_tweet(text=f"Faltam {dias_faltando} dias para o Vasco3 entrar em campo contra o(a) {oponente} pelo(a) {competicao}.")
        elif dias_faltando == 1:
            client.create_tweet(text=f"Falta {dias_faltando} dia para o Vasco entrar em campo contra o(a) {oponente} pelo(a) {competicao}.")
        else:
            client.create_tweet(text=f"Hoje tem Vasco! O Gigante da colina entra em campo contra o(a) {oponente} pelo(a) {competicao} às {hora}.")

    print("Tweet feito!")

# Cria um agendador
scheduler = BlockingScheduler()

# Adiciona a tarefa ao agendador para ser executada todos os dias às 11:00
scheduler.add_job(postar_tweet, 'cron', hour=11)

# Inicia o agendador
scheduler.start()