import telegram
import urllib
import urllib3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config
import json

keyboard_height = [[telegram.KeyboardButton('150'),
                    telegram.KeyboardButton('155'),
                    telegram.KeyboardButton('160'),
                    telegram.KeyboardButton('165'),
                    telegram.KeyboardButton('170'),
                    telegram.KeyboardButton('175')],
                   [telegram.KeyboardButton('180'),
                    telegram.KeyboardButton('185'),
                    telegram.KeyboardButton('190'),
                    telegram.KeyboardButton('195'),
                    telegram.KeyboardButton('200'),
                    ]]

keyboard_screen = [[telegram.KeyboardButton('4'),
                    telegram.KeyboardButton('4.3'),
                    telegram.KeyboardButton('4.5'),
                    telegram.KeyboardButton('4.7'),
                    telegram.KeyboardButton('4.8'),
                    telegram.KeyboardButton('5')],
                   [telegram.KeyboardButton('5.1'),
                    telegram.KeyboardButton('5.3'),
                    telegram.KeyboardButton('5.5'),
                    telegram.KeyboardButton('5.7'),
                    telegram.KeyboardButton('6.44'),
                    ]]

keyboard_symbol_line = [[telegram.KeyboardButton('1'),
                         telegram.KeyboardButton('2'),
                         telegram.KeyboardButton('3'),
                         telegram.KeyboardButton('4')],
                        [telegram.KeyboardButton('5'),
                         telegram.KeyboardButton('6'),
                         telegram.KeyboardButton('7'),
                         telegram.KeyboardButton('8')],
                        [telegram.KeyboardButton('9'),
                         telegram.KeyboardButton('10'),
                         telegram.KeyboardButton('11'),
                         telegram.KeyboardButton('12'),
                         ]]


def reply(msg=None, img=None):
    if msg:
        resp = urllib.urlopen('https://yandex.ru/search/?text=how%20to%20use%20inline%20keyboard%20python&&lr=213' + 'sendMessage', urllib.urlencode({
            'chat_id': str(update.message.chat_id),
            'text': msg.encode('utf-8'),
            'disable_web_page_preview': 'true',
            # 'reply_to_message_id': str(message_id),
            'reply_markup': json.dumps({'inline_keyboard': [
                [{'text': 'bline1', 'callback_data': 'bline1'}, {'text': 'bline2', 'callback_data': 'bline2'}]]}),
        })).read()