from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# Кнопки поддержки по работе с mysupport
inline_btn_1 = InlineKeyboardButton('Проверить гарантию', callback_data='button1', url='https://anton-kyrylenko.gitbook.io/tets/')
inline_btn_2 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='https://app.gitbook.com/@anton-kyrylenko/s/tets/obrashenie-v-tekh.-podderzhku-netapp/~/settings/advanced')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1,inline_btn_2)

# конпки поддержки по работе с Volume

