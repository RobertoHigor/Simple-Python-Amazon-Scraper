__author__ = "Roberto Higor Matos dos Anjos"

from bs4 import BeautifulSoup # Parser
import requests
import csv

# Armazenando o html
source = requests.get('https://www.amazon.com.br/s?k=iphone').text
soup = BeautifulSoup(source,'html5lib')

csv_file = open('scrape_amazon.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Nome', 'Preço'])

# Assim é possível achar algo específico
for produto in soup.find_all('div', class_='s-result-item'):  
    # O último produto pode retornar NoneType
    try:
        nome_produto = produto.h2.a.span.text
    except Exception as e:
        continue  
    
    # Nem todos os produtos tem preço
    try:
        preco_produto = produto.find('span', class_='a-offscreen').text        
    except Exception as e:
        #preco_produto = None
        continue   

    csv_writer.writerow([nome_produto, preco_produto])
csv_file.close()
