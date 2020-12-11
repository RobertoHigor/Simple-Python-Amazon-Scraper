# https://www.youtube.com/watch?v=ng2o98k983k
from bs4 import BeautifulSoup # Parser
import requests

# Armazenando o html
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source,'html5lib')

# soup.find() permite passar argumentos como classe e id.
# Assim é possível achar algo específico
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.find('div', class_='entry-content').p.text
    print(summary)  

    # Alguns posts podem não ter um link para video
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)
    print()
