
import re
import requests

# URL da agenda de jogos do Vasco do Globo Esporte
url = "https://ge.globo.com/futebol/times/vasco/agenda-de-jogos-do-vasco/#/"

# Solicitação para obter o código fonte da página
response = requests.get(url)
html_content = response.text

# Usando expressões regulares para encontrar a primeira ocorrência entre "match" e "location"
proximo_jogo_oponente = re.search(r'match.*?location"', html_content, re.DOTALL | re.UNICODE)

# Se encontrou a correspondência, extraia as instâncias após "popularName" entre aspas
if proximo_jogo_oponente:
    proximo_jogo_texto = proximo_jogo_oponente.group(0)
    
    # Usando expressão regular para encontrar todas as instâncias após "popularName" entre aspas
    times = re.findall(r'popularName":"(.*?)"', proximo_jogo_texto)

    # Verificando a instância diferente de "Vasco" e armazenando em "oponente"
    oponente = next((instancia for instancia in times if instancia != "Vasco"), None)

    # Se encontrou a correspondência, imprima o resultado
    if oponente:
        oponente= oponente.encode('latin1').decode('unicode_escape') 
        print(f"Oponente: {oponente}")
