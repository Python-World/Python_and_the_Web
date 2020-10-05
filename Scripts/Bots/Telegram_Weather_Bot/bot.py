import requests
import json
import configparser as cfg

class telegram_chatbot():

	def __init__(self, config):
		self.token = self.read_config(config)
		self.base = f'https://api.telegram.org/bot{self.token}/'
	
	def get_updates(self, offset=None):
		url = self.base + 'getUpdates?timeout=100'
		if offset:
			url = url + f'&offset={offset+1}'
		res = requests.get(url)
		return json.loads(res.content)
	
	def send_message(self, msg, chat_id):
		url = self.base + f'sendMessage?chat_id={chat_id}&text={msg}'
		if msg is not None:
			requests.get(url)

	@staticmethod
	def read_config(config):
		parser = cfg.ConfigParser()
		parser.read(config)
		return parser.get('creds', 'token')
