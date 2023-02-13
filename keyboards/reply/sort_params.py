from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def sort_params() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(True, True)
    keyboard.add(KeyboardButton('По возрастанию, ежеквартально'))
    keyboard.add(KeyboardButton('По убыванию, ежеквартально'))
    keyboard.add(KeyboardButton('По возрастанию, ежегодно'))
    keyboard.add(KeyboardButton('По убыванию, ежегодно'))
    return keyboard
