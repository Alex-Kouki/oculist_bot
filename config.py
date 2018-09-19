import telegram
# import eye_checker

# Выбор режима
keyboard_start = [[telegram.KeyboardButton('Проверка остроты зрения')],
                  [telegram.KeyboardButton('Проверка цветовосприятия глаза')]]

# Режим остроты зрения
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

keyboard_sex = [[telegram.KeyboardButton('Мужчина')],
                [telegram.KeyboardButton('Женщина')]]


