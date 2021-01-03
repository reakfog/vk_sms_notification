import time
import os
import requests

from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()
VK_API_VERSION = os.getenv('VK_API_VERSION')
VK_TOKEN = os.getenv('VK_TOKEN')
TWILIO_CLIENT = Client(os.getenv('TWILIO_SID'), os.getenv('TWILIO_TOKEN'))
NUMBER_FROM = os.getenv('NUMBER_FROM')
NUMBER_TO = os.getenv('NUMBER_TO')
API_URL = 'https://api.vk.com/method/users.get'


def get_status(user_id):
    params = {
        'user_ids': user_id,
        'v': VK_API_VERSION,
        'access_token': VK_TOKEN,
        'fields': 'online'
    }
    try:
        user_status = requests.post(API_URL, params=params)
        return user_status.json().get('response')[0].get('online')
    except requests.exceptions.RequestException as error:
        print(error)

# send_sms
def sms_sender(sms_text):
    client = TWILIO_CLIENT
    message = client.messages.create(
        body=sms_text,
        from_=NUMBER_FROM,
        to=NUMBER_TO
    )
    return message.sid


if __name__ == '__main__':
    vk_id = input('Введите id: ')
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
