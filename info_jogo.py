import re
import requests
from datetime import datetime

# URL da agenda de jogos do Vasco do Globo Esporte
url = "https://ge.globo.com/futebol/times/vasco/agenda-de-jogos-do-vasco/#/"

# Solicitação para obter o código fonte da página
response = requests.get(url)
html_content = response.text

# Usando expressões regulares para encontrar a primeira ocorrência entre "match" e "winner"
proximo_jogo_info = re.search(r'match.*?winner"', html_content, re.DOTALL | re.UNICODE)

# Se encontrou a correpondência
if proximo_jogo_info:
    proximo_jogo_info_texto = proximo_jogo_info.group(0)
    print(proximo_jogo_info_texto)

    # Usando expressão regular para encontrar as instâncias entre aspas após "name", "startDate" e "startHour"
    competicao = re.search(r'Championship","name":"([^"]+)"', proximo_jogo_info_texto)
    if competicao:
        competicao=competicao.group(1)
        print(competicao)
    dia = re.search(r'startDate":"([^"]+)"', proximo_jogo_info_texto)
    print(dia)
    hora = re.search(r'startHour":"([^"]+)"', proximo_jogo_info_texto)

    # Se encontrou a correspondência, imprima os resultados
    if competicao and dia and hora:
        
        dia = dia.group(1)
        hora = datetime.strptime(hora.group(1), "%H:%M:%S").strftime("%H:%M")
        competicao= competicao.encode('latin1').decode('unicode_escape') 
        print(f"Competição: {competicao}, Dia: {dia}, Hora: {hora}")