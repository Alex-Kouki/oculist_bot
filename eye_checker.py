#  Импортирую необходимые билбиотеки
import telegram
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config
import computing


# Discription of function Start
def start(bot, update):
    users[update.message.chat_id] = {'height': None, 'screen': None, 'left': None, 'right': None}
    # Inline keyboard
    # keyboard = [[telegram.InlineKeyboardButton("acuity", callback_data='/start')],
    #             [telegram.InlineKeyboardButton("color perception", callback_data='168')]]
    # reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    # update.message.reply_text('Выбери режим:', reply_markup=reply_markup)
    # update.message.reply_text(telegram.CallbackQuery)

    # name_button = 'fapacca'
    # keyboard = []
    #
    # for i in range(3):
    #     link = 'https://vk.com'
    #     keyboard.append([telegram.InlineKeyboardButton(text=artist,
    #                                                    url=link)])
    #
    # markup = telegram.InlineKeyboardMarkup(keyboard)
    # bot.sendMessage(chat_id=update.message.chat_id,
    #                 text="Check this out:",
    #                 reply_markup=markup)

    # отправка сообщения после нажатия /start
    update.message.reply_text('Привет! Этот бот проверит твое зрение, а так же даст рекомендации.'
                              'Ответьте на следующие вопросы:')
    # creating the keyboard
    markup = telegram.ReplyKeyboardMarkup(config.keyboard_height, one_time_keyboard=True, resize_keyboard=True)
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Укажите Ваш рост в сантиметрах (только цифры)",
                    reply_markup=markup)
    return


def height_screen(bot, update):
    user_message = update.message.text
    try:
        user_message = float(user_message)
    except:
        update.message.reply_text('Введите число')
        return
    # Если в значении по ключу рост пусто, то:
    if users[update.message.chat_id]['height'] is None:
        # если введенный рост входит в не обходимый диапазон:
        if 150 <= user_message <= 200:
            users[update.message.chat.id]['height'] = user_message
            # Вводим клавиатуру для ввода размера экрана
            markup = telegram.ReplyKeyboardMarkup(config.keyboard_screen, one_time_keyboard=True, resize_keyboard=True)
            bot.sendMessage(chat_id=update.message.chat_id,
                            text="Укажите диагональ экрана вашего смартфона (от 4 до 7)",
                            reply_markup=markup)
        else:
            markup = telegram.ReplyKeyboardMarkup(config.keyboard_height, one_time_keyboard=True, resize_keyboard=True)
            bot.sendMessage(chat_id=update.message.chat_id,
                            text='Укажите Ваш рост в сантиметрах от 150 до 200 см (только цифры)',
                            reply_markup=markup)
        return

    elif users[update.message.chat_id]['screen'] is None:
        # Если размер экрана введен корректно, то добавляем в users['screen']
        if 4.0 <= user_message <= 7.0:
            users[update.message.chat_id]['screen'] = user_message
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

            markup = telegram.ReplyKeyboardMarkup(config.keyboard_symbol_line, one_time_keyboard=True,
                                                  resize_keyboard=True)
            bot.sendMessage(chat_id=update.message.chat_id,
                            text="Укажите номер ряда с наименьшим размером букв, который "
                                 "Вам удалось верно прочесть левым глазом)",
                            reply_markup=markup)
        else:
            markup = telegram.ReplyKeyboardMarkup(config.keyboard_screen, one_time_keyboard=True, resize_keyboard=True)
            bot.sendMessage(chat_id=update.message.chat_id,
                            text='напиши число, соответствующее диагонали твоего смартфона',
                            reply_markup=markup)
        return

    elif users[update.message.chat_id]['left'] is None:
        if 0 <= user_message <= 12:
            users[update.message.chat.id]['left'] = user_message
            # клавиатура для указания ряда для правого глаза
            markup = telegram.ReplyKeyboardMarkup(config.keyboard_symbol_line, one_time_keyboard=True, resize_keyboard=True)
            bot.sendMessage(chat_id=update.message.chat_id,
                            text="Укажите номер ряда с наименьшим размером букв, который "
                                 "вам удалось верно прочесть правым глазом)",
                            reply_markup=markup)
        else:
            markup = telegram.ReplyKeyboardMarkup(config.keyboard_symbol_line, one_time_keyboard=True, resize_keyboard=True)
            bot.sendMessage(chat_id=update.message.chat_id,
                            text='напишите число, соответствующее наименьшему ряду, который вы смогли'
                                 'разглядеть левым глазом',
                            reply_markup=markup)
        return

    elif users[update.message.chat_id]['right'] is None:
        if 0 <= user_message <= 12:
            users[update.message.chat.id]['right'] = int(update.message.text)
            # начинаем расчет остроты зрения
            # left_acuity = users[update.message.chat.id]['left']


        else:
            markup = telegram.ReplyKeyboardMarkup(config.keyboard_symbol_line, one_time_keyboard=True,
                                                  resize_keyboard=True)
            bot.sendMessage(chat_id=update.message.chat_id,
                            text='напишите число, соответствующее наименьшему ряду, который вы смогли'
                                 'разглядеть правым глазом',
                            reply_markup=markup)
        return users

    elif users[update.message.chat_id]['right'] is not None:
        return

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

