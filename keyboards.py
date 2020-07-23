from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# Кнопки поддержки по работе с mysupport
inline_btn_1 = InlineKeyboardButton('Проверить гарантию', callback_data='button1', url='https://anton-kyrylenko.gitbook.io/tets/')
inline_btn_2 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='https://app.gitbook.com/@anton-kyrylenko/s/tets/obrashenie-v-tekh.-podderzhku-netapp')
inline_btn_3 = InlineKeyboardButton('Рег. системы', callback_data='button3', url='')
#inline_btn_4 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
#inline_btn_5 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
inline_kb1 = InlineKeyboardMarkup(row_width=2).add(inline_btn_1,inline_btn_2,inline_btn_3)

# конпки поддержки по работе с ontap_basic
ontap_btn_1 = InlineKeyboardButton('Как бновить ПО', callback_data='button1', url='')
ontap_btn_2 = InlineKeyboardButton('Обновить сертификат', callback_data='button2', url='')
ontap_btn_3 = InlineKeyboardButton('Восстановить пароль', callback_data='button2', url='')
#inline_btn_4 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
#inline_btn_5 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
ontap_kb1 = InlineKeyboardMarkup(row_width=2).add(ontap_btn_1,ontap_btn_2,ontap_btn_3)

# конпки поддержки по работе с ontap_special
spec_btn_1 = InlineKeyboardButton('Как бновить ПО', callback_data='button1', url='')
spec_btn_2 = InlineKeyboardButton('Обновить сертификат', callback_data='button2', url='')
spec_btn_3 = InlineKeyboardButton('Восстановить пароль', callback_data='button2', url='')
#inline_btn_4 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
#inline_btn_5 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
spec_kb1 = InlineKeyboardMarkup(row_width=2).add(ontap_btn_1,ontap_btn_2,ontap_btn_3)

# конпки поддержки по работе с e-series
eser_btn_1 = InlineKeyboardButton('Как бновить ПО', callback_data='button1', url='')
eser_btn_2 = InlineKeyboardButton('Обновить сертификат', callback_data='button2', url='')
eser_btn_3 = InlineKeyboardButton('Восстановить пароль', callback_data='button2', url='')
#inline_btn_4 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
#inline_btn_5 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
eseris_kb1 = InlineKeyboardMarkup(row_width=2).add(ontap_btn_1,ontap_btn_2,ontap_btn_3)

# конпки поддержки по работе с portfolio
port_btn_1 = InlineKeyboardButton('Как бновить ПО', callback_data='button1', url='')
port_btn_2 = InlineKeyboardButton('Обновить сертификат', callback_data='button2', url='')
port_btn_3 = InlineKeyboardButton('Восстановить пароль', callback_data='button2', url='')
#inline_btn_4 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
#inline_btn_5 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
port_kb1 = InlineKeyboardMarkup(row_width=2).add(ontap_btn_1,ontap_btn_2,ontap_btn_3)

# конпки поддержки по работе с design
des_btn_1 = InlineKeyboardButton('Как бновить ПО', callback_data='button1', url='')
des_btn_2 = InlineKeyboardButton('Обновить сертификат', callback_data='button2', url='')
des_btn_3 = InlineKeyboardButton('Восстановить пароль', callback_data='button2', url='')
#inline_btn_4 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
#inline_btn_5 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
design_kb1 = InlineKeyboardMarkup(row_width=2).add(ontap_btn_1,ontap_btn_2,ontap_btn_3)
