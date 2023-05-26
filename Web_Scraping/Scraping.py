import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math
from unidecode import unidecode


url = 'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
qnt_itens = soup.find('div', id='listingCount').get_text().strip()

index = qnt_itens.find(' ')
qnt = qnt_itens[:index]

ultima_pagina = math.ceil(int(qnt) / 20)

dic_produtos = {'marca': [], 'preco': []}

for i in range(1, ultima_pagina + 1):
    url_pag = f'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer?gclid=CjwKCAjwgqejBhBAEiwAuWHioHAidlgIhJ8lx95oLyJ5xsuY7bjVqkEXK_mXBFsGmq5yHe8V1ftfGxoCOBYQAvD_BwE&page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    produtos = soup.find_all('div', class_=re.compile('productCard'))

    for produto in produtos:
        marca = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
        preco = produto.find('span', class_=re.compile('priceCard')).get_text().strip()

        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(preco)

df = pd.DataFrame(dic_produtos)

df['preco']= df['preco'].apply(lambda x: unidecode(x))
df['marca'] = df['marca'].apply(lambda x: unidecode(x))
df.rename(columns={'preco': 'Valor'}, inplace=True)
df.rename(columns={'marca': 'Marca'}, inplace=True)
df['Marca'] = df['Marca'].str.replace('cadeira', '', case=False)
df.to_string(index=False)



df.to_csv(r'C:\Users\Bruno Xavier\Desktop\Data Enginer\Curso Web Scraping\Kabum\kabum.csv', encoding='utf-8', sep=';')


