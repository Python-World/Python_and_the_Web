# telebot and telethon modules are required
import telebot 
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import sync, events 
  
   
# Enter the API token in 'token'.
# Enter the API ID and API Hash from
# the telegram app created.
api_id = 'API_id'
api_hash = 'API_hash'
token = 'bot token'
  
# your phone number 
phone = 'YOUR_PHONE_NUMBER_WTH_COUNTRY_CODE'
   
# creating a telegram session and assigning 
# it to a variable client 
client = TelegramClient('session', api_id, api_hash) 
   
# connecting and building the session 
client.connect() 
  
# in case of script ran first time it will 
# ask either to input token or otp sent to 
# number or sent or your telegram id  
if not client.is_user_authorized(): 
   
    client.send_code_request(phone) 
      
    # signing in the client 
    client.sign_in(phone, input('Enter the code: ')) 
   
   
try: 
    # receiver user_id and access_hash 
    receiver = InputPeerUser('user_id', 'user_hash') 
  
    # sending message using telegram client 
    client.send_message(receiver, "Hello", parse_mode='html')
except Exception as e: 
      
    # there may be many error coming in while like peer 
    # error, wwrong access_hash, flood_error, etc 
    print(e); 
  
# disconnecting the telegram session  
client.disconnect()
