import time

import requests
from twilio.rest import Client

# здесь проинициализируйте Client 

def get_status(user_id):
    params = {
        ...
    }
    ...
    return ...  # Верните статус пользователя в ВК


def send_sms(sms_text):
    ...
    return ...  # Верните sid отправленного сообщения из Twilio


if __name__ == '__main__':
    vk_id = input('Введите id ')
    while True:
        if get_status(vk_id) == 1:
            send_sms(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
