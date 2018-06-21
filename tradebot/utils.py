# -*- coding: utf-8 -*-
import json
import requests

BASE_URL = 'https://api.iextrading.com/1.0/stock/{ticker}/chart/{period}'


def pulldata(ticker, period='1y'):
    url = BASE_URL.format(ticker=ticker, period=period)
    r = requests.get(url)
    return json.loads(r.text)


if __name__ == '__main__':
    pulldata('aapl')

