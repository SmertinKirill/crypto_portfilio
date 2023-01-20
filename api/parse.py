import requests
from bs4 import BeautifulSoup

f = open('curr.txt', 'w')

for x in range(1, 10):
    url = f'https://www.coingecko.com/?page={x}'

    headers = {
        'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    resp = requests.get(url, headers=headers).text
    soup = BeautifulSoup(resp, 'lxml')

    tbody = soup.find('tbody')
    coins = tbody.find_all('tr')

    for coin in coins:
        full = coin.find(class_='py-0 coin-name cg-sticky-col cg-sticky-third-col px-0').get('data-sort')
        symbol = coin.find(class_='pl-1 pr-0 cg-sticky-col cg-sticky-first-col').find('i').get('data-coin-symbol')
        f.write(f"('{symbol.upper()}', '{full}'),\n")

f.close()
