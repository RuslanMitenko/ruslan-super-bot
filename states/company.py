from telebot.handler_backends import State, StatesGroup


class CompanyInfoState(StatesGroup):
    name = State()
