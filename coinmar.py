import json
import requests
from datetime import datetime

currency='INR'


global_url='https://api.coinmarketcap.com/v2/global/?convert='+ currency


request=requests.get(global_url)
results=request.json()

#print(json.dumps(results,sort_keys=True,indent=4))

active_cryptocurrencies=results['data']['active_cryptocurrencies']
active_markets=results['data']['active_markets']
bitcoin_percentage_of_market_cap=results['data']['bitcoin_percentage_of_market_cap']
last_updated=results['data']['last_updated']
total_market_cap=int(results['data']['quotes'][currency]['total_market_cap'])
total_volume_24h=int(results['data']['quotes'][currency]['total_volume_24h'])

active_cryptocurrencies_string='{:,}'.format(active_cryptocurrencies)
active_markets_string='{:,}'.format(active_markets)
total_market_cap_string='{:,}'.format(total_market_cap)
total_volume_24h_string='{:,}'.format(total_volume_24h)

last_updated_string=datetime.fromtimestamp(last_updated).strftime('%d %B,%Y at %I:%M%p')

print()
print('There are currently '+active_cryptocurrencies_string+' active cryptocurrencies')
print('There are currently '+active_markets_string+' active markets')
print('The total global cap of crypto is '+total_market_cap_string+' and '+'The 24h total volume '+total_volume_24h_string+'.')
print()
print('Bitcoin percentage is '+str(bitcoin_percentage_of_market_cap)+'%')
print('The information was last updated on '+last_updated_string+'.')
