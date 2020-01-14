import json
import requests

while True:

	ticker_url='https://api.coinmarketcap.com/v2/ticker/?structure=array'

	limit=10
	start=1
	sort='id'
	convert='USD'

	choice=input("Do you want to enter custom parameters? (y/n): ")

	if choice=='y':

		limit=input('What is the custom limit?:')
		start=input('What is the custom start number?:')
		sort=input('By what you want to sort?:')
		convert=input('Whats your local currency?:')

	ticker_url +='&limit'+str(limit)+'&start'+str(start)+'&sort'+sort+'&convert'+convert

	request=requests.get(ticker_url)
	results=request.json()

	print(json.dumps(results,sort_keys=True,indent=4))

	data=results['data']

	print()
	for currency in data:

		name=currency['name']
		symbol=currency['symbol']
		rank=currency['rank']

		circulating_supply=int(currency['circulating_supply'])
		total_supply=int(currency['total_supply'])

		market_cap=currency['quotes']['USD']['market_cap']
		hour_change=str(currency['quotes']['USD']['percent_change_1h'])
		day_change=str(currency['quotes']['USD']['percent_change_24h'])
		percent_change_week=str(currency['quotes']['USD']['percent_change_7d'])
		price=str(currency['quotes']['USD']['price'])
		volume_day=currency['quotes']['USD']['volume_24h']

		market_cap_string='{:,}'.format(market_cap)
		volume_day_string='{:,}'.format(volume_day)
		circulating_supply_string='{:,}'.format(circulating_supply)
		total_supply_string='{:,}'.format(total_supply)

		print(str(rank)+':'+name+'('+symbol+')')
		print('Market cap:\t\t$'+market_cap_string)
		print('Price:\t\t\t$'+price)
		print('Volume 24H change:\t\t$'+volume_day_string)
		print('Circulating supply:\t$'+circulating_supply_string)
		print('Total supply:\t\t$'+total_supply_string)
		print('Hour change:\t\t$'+hour_change+'%')
		print('24h change:\t\t$'+day_change+'%')
		print('percent change 7d:\t\t$'+percent_change_week+'%')
		print('Percenatge of coins in circulations:'+str(int(circulating_supply/total_supply*100)))
		print()
	choice=input('Again?(y/n):')

	if choice=='n':
	   break