import json
import requests
from pprint import pprint
import re

# territory_id  = "2304400"
# keywords = "dispensa de licitação"
# start_date = "2021-01-01"
# endpoint = f"https://queridodiario.ok.org.br/api/cities/{territory_id}?keywords={keywords}&since={start_date}"

# response = requests.get(endpoint)

# pprint(json.loads(response.text))

ranking_filmes = []

with open('imdb.json', 'r') as arquivo:
    filmes = json.load(arquivo)
    
    for dicionarios in filmes:
        for chave, valor in dicionarios.items():
            if valor is not None:
                dicionarios[chave] = valor.strip()
                if chave == 'position':
                    dicionarios[chave] = valor.split('\n')[0]
                if chave == 'ano_lancamento':
                    ano = re.findall(r'[0-9]', valor)
                    dicionarios[chave] = ''.join(ano)
            
        ranking_filmes.append(dicionarios)


with open('ranking_filmes.json', 'w') as arquivo:
    json.dump(ranking_filmes,arquivo,
              ensure_ascii=False,indent=2)
    
# requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
# dicionario = requisicao.json()
