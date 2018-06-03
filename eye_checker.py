#  Импортирую необходимые билбиотеки
import telegram
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Discription of function Start
def start(bot, update):
    print ('sanёk')
    users[update.message.chat_id] = {'height': None, 'screen': None, 'left': None, 'right': None}
    """Send a message when the command /start is issued."""
    update.message.reply_text('Привет! Этот бот проверит твое зрение, а так же даст рекомендации.'
                              ' Ответьте на следующие вопросы:')
    # creating the keyboard
    keyboard = [[telegram.KeyboardButton('150'),
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
    markup = telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Укажите Ваш рост в сантиметрах (только цифры)",
                    reply_markup=markup)
    # resume
    print(users)

def height_screen(bot, update):
    # Если в значении по ключу рост пусто, то:
    print('sanek lox')
    if users[update.message.chat_id] == {'height': None, 'screen': None, 'left': None, 'right': None}:
        # если введенный рост входит в необходимый диапазон:
        if 150 <= float(update.message.text) <= 200:
            users[update.message.chat.id]['height'] = int(update.message.text)
            print(users)
            # Вводим клавиатуру для ввода размера экрана
            keyboard = [[telegram.KeyboardButton('4'),
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
            markup = telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
            bot.sendMessage(chat_id=update.message.chat_id,
                            text="Укажите диагональ экрана вашего смартфона (от 4 до 7)",
                            reply_markup=markup)

    elif (users[update.message.chat_id]['height'] is not None
          and users[update.message.chat_id]['screen'] is None
          and users[update.message.chat_id]['right'] is None
          and users[update.message.chat_id]['left'] is None):
        # Если размер экрана введен корректно, то добавляем в users['screen']
        if 4.0 <= float(update.message.text) <= 7.0:
            users[update.message.chat_id]['screen'] = float(update.message.text)
            print(users)
            # We get the correct 'height' and 'screen'
            update.message.reply_text('Инструкция: Откройте изображение в полном размере,'
                                      'держите телефон в вертикальном положении на вытянутой руке на уровне глаз.'
                                      'Вы должны закрыть сначала правый глаз и прочитать буквы, находящиеся слева.'
                                      'Потом закройте левый глаз и прочтите буквы справа. Укажите номер ряда с '
                                      'наименьшим размером букв, который Вам удалось верно прочесть левым глазом,'
                                      ' а потом для правым')
            # Пауза для прочтения
            time.sleep(1)
            # Отправляю картинку
            bot.send_photo(chat_id=update.message.chat.id,
                           photo=open('/home/al/PycharmProjects/telegram/sivcev.jpg', 'rb'))
            # Пауза для прочтения
            time.sleep(1)
            # клавиатура для указания ряда для левого глаза
            keyboard = [[telegram.KeyboardButton('1'),
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
            markup = telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
            bot.sendMessage(chat_id=update.message.chat_id,
                            text="Укажите номер ряда с наименьшим размером букв, который "
                                 "Вам удалось верно прочесть левым глазом)",
                            reply_markup=markup)
    elif (users[update.message.chat_id]['height'] is not None
          and users[update.message.chat_id]['screen'] is not None
          and users[update.message.chat_id]['left'] is None
          and users[update.message.chat_id]['right'] is None):
        if 0 <= float(update.message.text) <= 12:
            users[update.message.chat.id]['left'] = int(update.message.text)
            print(users)
            # клавиатура для указания ряда для правого глаза
            keyboard = [[telegram.KeyboardButton('1'),
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
            markup = telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
            bot.sendMessage(chat_id=update.message.chat_id,
                            text="Укажите номер ряда с наименьшим размером букв, который "
                                 "Вам удалось верно прочесть правым глазом)",
                            reply_markup=markup)
            print(users)
    elif (users[update.message.chat_id]['height'] is not None
          and users[update.message.chat_id]['screen'] is not None
          and users[update.message.chat_id]['left'] is not None
          and users[update.message.chat_id]['right'] is None):
        if 0 <= float(update.message.text) <= 12:
            users[update.message.chat.id]['right'] = int(update.message.text)
    print(users)



    # # Или Если не указан рост,то:
    # elif (users[update.message.chat.id]['height'] is None) \
    #         and (users[update.message.chat.id]['screen'] is not None):
    #     update.message.reply_text('Укажите Ваш рост в сантиметрах от 150 до 200 см (только цифры)')
    # # Или Если не указан экран
    # elif (users[update.message.chat.id]['height'] is not None)\
    #         and (users[update.message.chat.id]['screen'] is None):
    #     update.message.reply_text('Укажите диагональ экрана в дюймах от 4.0 до 7.0 (только цифры)')
    # # Или Если указан и рост и экран
    # elif ((users[update.message.chat.id]['height'] is not None)
    #       and (users[update.message.chat.id]['screen'] is not None)):
    #     update.message.reply_text('Все данные собраны!')


def main():
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


users = {}
main()

