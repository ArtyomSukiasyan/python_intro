import requests
from bs4 import BeautifulSoup

url = 'https://ararat.chessnews.am/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('h2')

    for idx, article in enumerate(articles, 1):
        title = article.text.strip()
        print(f"{idx}. {title}")
else:
    print(
        f"Failed to retrieve the webpage. Status code: {response.status_code}")
