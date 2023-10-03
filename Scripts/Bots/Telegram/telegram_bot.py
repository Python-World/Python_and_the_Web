from configparser import ConfigParser

from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser

configur = ConfigParser()
configur.read("config.ini")

# Enter the API token in 'token'.
# Enter the API ID and API Hash from
# the telegram app created.
api_id = configur.get("app_config", "api_id")
api_hash = configur.get("app_config", "api_hash")
token = configur.get("bot_api", "token")

# your phone number
phone = configur.get("client_details", "phone")

# client variable
client = None

# receiver user_id and access_hash
user_id = configur.get("receiver_details", "user_id")
user_hash = configur.get("receiver_details", "user_hash")


def client_connect(client):
    # creating a telegram session and assigning
    # it to a variable client
    client = TelegramClient("session", api_id, api_hash)

    # connecting and building the session
    client.connect()


def client_authenticate(client, phone):
    # in case of script ran first time it will
    # ask either to input token or otp sent to
    # number or sent or your telegram id
    if not client.is_user_authorized():
        client.send_code_request(phone)

        # signing in the client
        client.sign_in(phone, input("Enter the code: "))


def messasge_send(client, user_id, user_hash):
    try:
        receiver = InputPeerUser(user_id, user_hash)

        # sending message using telegram client
        client.send_message(receiver, "Hello", parse_mode="html")
    except Exception as e:
        # there may be many error coming in while like peer
        # error, wwrong access_hash, flood_error, etc
        print(e)


def client_disconnect(client):
    # disconnecting the telegram session
    client.disconnect()


client_connect(client)

client_authenticate(client, phone)

client_disconnect(client)
