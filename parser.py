import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.de/-/en/Apple-Watch-GPS-Aluminium-AppleCare/dp/B09YJ3N3QD/ref=sr_1_1?keywords=apple%2Bwatch&qid=1652970493&sr=8-1&th=1'
headers = {
'authority': 'www.amazon.com',
'pragma': 'no-cache',
'cache-control': 'no-cache',
'dnt': '1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-dest': 'document',
'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, "html.parser")
price = soup.find(id="attach-base-product-price")
print(price['value'])
