from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def fin_info_params() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(True, True)
    keyboard.add(KeyboardButton('Доход (revenue)'))
    keyboard.add(KeyboardButton('Операционные расходы (operating expense)'))
    keyboard.add(KeyboardButton('Чистая прибыль (net income)'))
    keyboard.add(KeyboardButton('Рентабельность по чистой прибыли (net profit margin)'))
    keyboard.add(KeyboardButton('Прибыль на акцию (earning per share)'))
    keyboard.add(KeyboardButton('EBITDA'))
    return keyboard
