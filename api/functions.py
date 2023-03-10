import json
import os
from decimal import Decimal

from django.db.models import Sum
from dotenv import load_dotenv
from requests import Session

from portfolio.models import Buy, Sell

load_dotenv()


def get_price(tag):
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

    parametrs = {
        'symbol': tag,
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': os.getenv('API_KEY')
    }
    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parametrs)
    data = json.loads(response.text)
    global current_price
    current_price = data['data'][tag][0]['quote']['USD']['price']
    return round(current_price, 3)


def get_total(user_id, currency):
    buy = Buy.objects.filter(user_id=user_id, currency=currency)
    global sum_buy
    sum_buy = buy.aggregate(Sum('count'))['count__sum']
    sell = Sell.objects.filter(user_id=user_id, currency=currency)
    global sum_sell
    sum_sell = sell.aggregate(Sum('count'))['count__sum']
    if not sum_sell:
        sum_sell = 0
    if sum_buy:
        global total
        total = sum_buy - sum_sell
        holdings = total * Decimal(current_price)
        return [f'{round(total, 3)} {currency}', f'{round(holdings, 3)}$']
    return '—'


def get_profit(user_id, currency):
    amount_buy = Buy.objects.filter(user_id=user_id, currency=currency)
    sum_amount_buy = amount_buy.aggregate(Sum('amount'))['amount__sum']
    amount_sell = Sell.objects.filter(user_id=user_id, currency=currency)
    if not amount_buy or total == 0:
        return '—'

    if not amount_sell:
        profit = round(
            (
                (total * Decimal(current_price) - sum_amount_buy)
                / sum_amount_buy
            ) * 100, 2
        )
    else:
        sum_count = amount_buy.aggregate(Sum('count'))['count__sum']
        sum_amount_sell = amount_sell.aggregate(Sum('amount'))['amount__sum']
        average_purchase = sum_amount_buy / sum_count
        total_money = total * Decimal(current_price)
        profit_money = total_money - (sum_amount_buy - sum_amount_sell)
        profit = round(
            (profit_money / average_purchase) * 100, 2
        )
        print(profit)
    profit_money = round(profit_money, 2)
    if profit >= 0:
        return f'+{profit_money}$ | +{profit}%'
    return f'-{profit_money}$ | -{profit}%'
