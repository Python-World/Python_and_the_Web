from bot import telegram_chatbot
from weather import weather_info

bot = telegram_chatbot('telegram_config.cfg')
wi = weather_info('owm_config.cfg')

def make_reply(message):
	reply = None
	if message is not None:
		stats = wi.get_info(message)
	if message in ('/start', '/help'):
		reply = "Enter a city name in chat to get its real time weather stats\nSend '/help' in case of unexpected behaviour or difficulties\n\nNote: Make sure you enter a 'valid city name' and not any state or country name, doing so will result in improper replies"
		return reply
	if str(stats['cod']) == '404':
		return 'City not found. Enter a valid city name'
	reply = []
	reply.append(stats['name'])
	reply.append(f"Description: {stats['weather'][0]['description']}")
	reply.append(f"Temperature(celcius): {round(stats['main']['temp'] - 273.15, 2)}")
	reply.append(f"Max Temperature(celcius): {round(stats['main']['temp_max'] - 273.15, 2)}")
	reply.append(f"Min Temperature(celcius): {round(stats['main']['temp_min'] - 273.15, 2)}")
	reply.append(f"Humidity(percent): {stats['main']['humidity']}")
	reply.append(f"Pressure(hPa): {stats['main']['pressure']}")
	reply = '\n'.join(reply)
	return reply

update_id = None
while True:
	print('...')
	updates = bot.get_updates(offset=update_id)
	updates = updates['result']
	if updates:
		for item in updates:
			update_id = item['update_id']
			try:
				message = item['message']['text']
			except:
				message = None
			from_ = item['message']['chat']['id']
			reply = make_reply(message)
			bot.send_message(reply, from_)
