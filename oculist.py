#  Импортирую необходимые билбиотеки
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters\



def start(bot, update):
    update.message.reply_text('Привет, этот бот может проверить твое на остроту и цветовосприятие, а так же дать '
                              'рекомендации')
def height_screen(bot, update):
    x = 0
    if x = 0:








def main(bot):
    updater = Updater("598361564:AAFx-LArh5brPzPY8PPpxq7Te_8fn9k-SOw")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # if handler start WITH /(command)
    dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(CommandHandler("help", help))

    # if handler start WITHOUT /
    dp.add_handler(MessageHandler(Filters.text, height_screen))

# Start the Bot
    updater.start_polling()

# Run the bot
    updater.idle()

users = {'height': None, 'screen': None}
main()