from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from telegram import bot

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Привет! Этот бот проверит твое зрение, а так же даст рекомендации. Ответьте на следующие вопросы:')
    update.message.reply_text('Укажите Ваш рост в сантиметрах (только цифры)')
    print(update)
    print(update.message.chat.id)
    user_parameters[update.message.chat.id] = {'height': None,
                       'screen': None}

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Укажите рост и диагональ экрана телефона')

user_parameters = {}


def height_screen(bot, update):
    message = update.message.text
    if user_parameters[update.message.chat.id]['height'] is None:
        if 150 <= int(message) <= 200:
            user_parameters[update.message.chat.id]['height'] = int(message)
            update.message.reply_text('Теперь введи размер своего дисплея')
            pass
        else:
            update.message.reply_text('Введи свой рост в сантиметрах, он должен быть от 150 до 200')
            user_parameters[update.message.chat.id]['height'] = float(message)
            print(user_parameters)
    elif user_parameters[update.message.chat.id]['screen'] is None:
        if 4.0 <= float(message) <= 7.0:
            user_parameters[update.message.chat.id]['screen'] = float(message)
            update.message.reply_text('Отлично')
            print(user_parameters)
        else:
            update.message.reply_text('Введи размер дисплея в дюймах, он долженo быть от 4 до 7')


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("598361564:AAFx-LArh5brPzPY8PPpxq7Te_8fn9k-SOw")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # Ввод данных
    dp.add_handler(MessageHandler(Filters.text, height_screen))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()