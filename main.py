import requests
import pandas as pd

from bs4 import BeautifulSoup
from os.path import exists



header_list = []
body_list = []

def populate_fiis_list():
    html_text = requests.get('https://www.fundsexplorer.com.br/ranking').text
    soup = BeautifulSoup(html_text,'lxml')

    table_ranking = soup.find('table',id='table-ranking')
    table_head_itens = table_ranking.thead.tr.find_all('th')
    table_body_itens = table_ranking.tbody.find_all('tr')
    for item in table_head_itens:
        header_list.append(item.text)

    for item in table_body_itens:
        body_list.append(item.text.strip().split('\n'))



df = pd.DataFrame(columns=header_list)
for index,item in enumerate(body_list):
     df.loc[index] = item

file_exists  = exists("list/list_fiis.csv")

if not file_exists:
    df.to_csv("list/list_fiis.csv")