from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# Кнопки поддержки по работе с mysupport
inline_btn_1 = InlineKeyboardButton('Проверить гарантию', callback_data='button1', url='https://anton-kyrylenko.gitbook.io/tets/')
inline_btn_2 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='https://app.gitbook.com/@anton-kyrylenko/s/tets/obrashenie-v-tekh.-podderzhku-netapp')
inline_btn_3 = InlineKeyboardButton('Рег. системы', callback_data='button3', url='https://app.gitbook.com/@anton-kyrylenko/s/tets/mysupport/operacii-s-akkauntom')
inline_btn_4 = InlineKeyboardButton('Таблица сервисов', callback_data='button4', url='https://drive.google.com/file/d/1MNOpB0tPnHroPhtrmfhTEDiNvkYLuBWF/view?usp=sharing')
#inline_btn_5 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
inline_kb1 = InlineKeyboardMarkup(row_width=2).add(inline_btn_1,inline_btn_2,inline_btn_3)

# конпки поддержки по работе с ontap_basic
ontap_btn_1 = InlineKeyboardButton('Как скачать прошивку', callback_data='button1', url='https://app.gitbook.com/@anton-kyrylenko/s/tets/ontap/untitled-1')
ontap_btn_2 = InlineKeyboardButton('Как обновить прошивку', callback_data='button2', url='https://app.gitbook.com/@anton-kyrylenko/s/tets/ontap/untitled')
ontap_btn_3 = InlineKeyboardButton('AutoSupport', callback_data='button3', url='https://app.gitbook.com/@anton-kyrylenko/s/tets/ontap/kak-nastroit-autosupport')
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
#eser_btn_1 = InlineKeyboardButton('Как бновить ПО', callback_data='button1', url='')
#eser_btn_2 = InlineKeyboardButton('Обновить сертификат', callback_data='button2', url='')
#eser_btn_3 = InlineKeyboardButton('Восстановить пароль', callback_data='button2', url='')
#inline_btn_4 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
#inline_btn_5 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
eseris_kb1 = InlineKeyboardMarkup(row_width=2).add(ontap_btn_1,ontap_btn_2,ontap_btn_3)

# конпки поддержки по работе с portfolio
port_btn_1 = InlineKeyboardButton('Преимущества ONTAP', callback_data='button1', url='https://app.gitbook.com/@anton-kyrylenko/s/tets/portfolio/untitled')
port_btn_2 = InlineKeyboardButton('FAS\AFF', callback_data='button2', url='https://app.gitbook.com/@anton-kyrylenko/s/tets/portfolio/netapp-fas-aff')
port_btn_3 = InlineKeyboardButton('E-series', callback_data='button3', url='https://app.gitbook.com/@anton-kyrylenko/s/tets/e-series')
#inline_btn_4 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
#inline_btn_5 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
port_kb1 = InlineKeyboardMarkup(row_width=2).add(ontap_btn_1,ontap_btn_2,ontap_btn_3)

# конпки поддержки по работе с design
#des_btn_1 = InlineKeyboardButton('Как бновить ПО', callback_data='button1', url='')
#des_btn_2 = InlineKeyboardButton('Обновить сертификат', callback_data='button2', url='')
#des_btn_3 = InlineKeyboardButton('Восстановить пароль', callback_data='button2', url='')
#inline_btn_4 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
#inline_btn_5 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
design_kb1 = InlineKeyboardMarkup(row_width=2).add(ontap_btn_1,ontap_btn_2,ontap_btn_3)
