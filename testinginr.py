import json
import requests
from datetime import datetime

currency='JPY'


global_url='https://api.coinmarketcap.com/v2/global/?convert='+ currency


request=requests.get(global_url)
results=request.json()

active_cryptocurrencies=results['data']['active_cryptocurrencies']
active_markets=results['data']['active_markets']
bitcoin_percentage_of_market_cap=results['data']['bitcoin_percentage_of_market_cap']
last_updated=results['data']['last_updated']
total_market_cap=int(results['data']['quotes'][currency]['total_market_cap'])
total_volume_24h=int(results['data']['quotes'][currency]['total_volume_24h'])
