import requests
import json
import configparser as cfg

class weather_info():

	def __init__(self, config):
		self.token = self.read_config(config)
		self.base = f'https://api.openweathermap.org/data/2.5/weather?appid={self.token}'
	
	def get_info(self, city):
		url = self.base + f'&q={city}'
		res = requests.get(url)
		return json.loads(res.content)
	
	@staticmethod
	def read_config(config):
		parser = cfg.ConfigParser()
		parser.read(config)
		return parser.get('creds', 'token')
