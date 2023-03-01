import json
from models import Crypto

with open('currency.json', 'r') as f:
    currencies = json.load(f)

cryptos = []
for symbol, name in currencies.items():
    crypto = Crypto(symbol=symbol, name=name)
    cryptos.append(crypto)

Crypto.objects.bulk_create(cryptos)