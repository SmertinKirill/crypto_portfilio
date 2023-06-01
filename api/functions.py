import json
import os
import requests
from decimal import Decimal

from django.db.models import Sum
from dotenv import load_dotenv
from requests import Session

from portfolio.models import Buy, Sell

load_dotenv()


def get_price(tag):
    """
    Считает текущую стоимость криптовалюты с помощью API Coinmarketcap.
    """
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
    try:
        response = session.get(url, params=parametrs)
        data = json.loads(response.text)
        global current_price
        current_price = data['data'][tag][0]['quote']['USD']['price']
        return round(current_price, 3)
    except (requests.RequestException, KeyError, ValueError) as e:
        raise Exception(
            'Ошибка при выполнении запроса или обработке данных'
        ) from e
    except Exception as e:
        raise Exception('Неизвестная ошибка') from e


def get_total(user_id, currency):
    """
    Считает общее количество криптовалюты(total) и выводит стоимость(holdings).
    """
    buy = Buy.objects.filter(user_id=user_id, currency=currency)
    sell = Sell.objects.filter(user_id=user_id, currency=currency)
    sum_buy = buy.aggregate(Sum('count'))['count__sum']
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
    """
    Расчитывает профит
    """
    amount_buy = Buy.objects.filter(user_id=user_id, currency=currency)
    amount_sell = Sell.objects.filter(user_id=user_id, currency=currency)
    sum_amount_buy = amount_buy.aggregate(Sum('amount'))['amount__sum']
    sum_amount_sell = amount_sell.aggregate(Sum('amount'))['amount__sum']
    if not amount_buy:
        return '—'
    total_money = Decimal(total) * Decimal(current_price)
    if not amount_sell:
        profit = round(
            (
                (total * Decimal(current_price) - sum_amount_buy)
                / sum_amount_buy
            ) * 100, 2
        )
        profit_money = total_money - sum_amount_buy
    else:
        sum_count = amount_buy.aggregate(Sum('count'))['count__sum']
        average_purchase = sum_amount_buy / sum_count
        profit_money = total_money - (sum_amount_buy - sum_amount_sell)
        profit = round(
            (profit_money / average_purchase) * 100, 2
        )
    profit_money = round(profit_money, 2)
    if profit >= 0:
        return f'+{profit_money}$ | +{profit}%'
    return f'{profit_money}$ | {profit}%'
