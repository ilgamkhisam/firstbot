import requests 
from datetime import datetime

import telebot 
from config import token



def telegram_bot(token):
    bit_bot = telebot.TeleBot(token)

    @bit_bot.message_handler(commands=['start'])  
    def start_message(message):
        bit_bot.send_message(message.chat.id, 'Привет! я узкоспециальный бот и знаю только одну команду `price` и это последняя цена Биткоина .')

    @bit_bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == 'price':
            try:

                req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
                response = req.json()
                sell_price = response['btc_usd']['sell']
                bit_bot.send_message(
                    message.chat.id,  
                    f'{datetime.now().strftime("%Y-%m-%d %H:%M")},\nSell BTC Price: {sell_price}$'
                    )

            except Exception as ex:
                bit_bot.send_message(
                    message.chat.id,
                    'Ошибка!'

                )
        else:
             bit_bot.send_message( 
                 message.chat.id,
                 "В данный момент доступен только вывод последней цены Биткоина по команде price! "
             )

    bit_bot.polling()


if __name__ == '__main__':
    telegram_bot(token) 