from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# Кнопки поддержки по работе с mysupport
inline_btn_1 = InlineKeyboardButton('Посмотреть серийный номер', callback_data='button1', url='https://app.gitbook.com/@anton-kyrylenko/s/netapp/mysupport/kak-uznat-seriinyi-nomer-sistemy')
inline_btn_2 = InlineKeyboardButton('Регистрация системы', callback_data='button2', url='https://app.gitbook.com/@anton-kyrylenko/s/netapp/mysupport/registraciya-sistemy')
inline_btn_3 = InlineKeyboardButton('Операции с аккаунтом', callback_data='button3', url='https://app.gitbook.com/@anton-kyrylenko/s/netapp/mysupport/operacii-s-akkauntom')
inline_btn_4 = InlineKeyboardButton('Обращение в тех. поддержку', callback_data='button4', url='https://app.gitbook.com/@anton-kyrylenko/s/netapp/mysupport/obrashenie-v-tekh.-podderzhku-netapp')
inline_btn_5 = InlineKeyboardButton('Проверить гарантию', callback_data='button5', url='https://app.gitbook.com/@anton-kyrylenko/s/netapp/mysupport/kak-posmotret-status-garantii-i-uroven-servisa-svoei-sistemy')
inline_btn_6 = InlineKeyboardButton('Active IQ', callback_data='button6', url='https://app.gitbook.com/@anton-kyrylenko/s/netapp/mysupport/active-iq')
inline_kb1 = InlineKeyboardMarkup(row_width=1).add(inline_btn_1,inline_btn_2,inline_btn_3,inline_btn_4,inline_btn_5,inline_btn_6)

# конпки поддержки по работе с ontap_basic
ontap_btn_1 = InlineKeyboardButton('Как скачать прошивку', callback_data='button1', url='https://is.gd/aPBNIH')
ontap_btn_2 = InlineKeyboardButton('Как обновить прошивку', callback_data='button2', url='https://is.gd/4VnZUr')
ontap_btn_3 = InlineKeyboardButton('AutoSupport', callback_data='button3', url='')
#inline_btn_4 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
#inline_btn_5 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
ontap_kb1 = InlineKeyboardMarkup(row_width=1).add(ontap_btn_1,ontap_btn_2,ontap_btn_3)

# конпки поддержки по работе с ontap_special
spec_btn_1 = InlineKeyboardButton('Как бновить ПО', callback_data='button1', url='')
spec_btn_2 = InlineKeyboardButton('Обновить сертификат', callback_data='button2', url='')
spec_btn_3 = InlineKeyboardButton('Восстановить пароль', callback_data='button2', url='')
#inline_btn_4 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
#inline_btn_5 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
spec_kb1 = InlineKeyboardMarkup(row_width=1).add(ontap_btn_1,ontap_btn_2,ontap_btn_3)

# конпки поддержки по работе с e-series
#eser_btn_1 = InlineKeyboardButton('Как бновить ПО', callback_data='button1', url='')
#eser_btn_2 = InlineKeyboardButton('Обновить сертификат', callback_data='button2', url='')
#eser_btn_3 = InlineKeyboardButton('Восстановить пароль', callback_data='button2', url='')
#inline_btn_4 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
#inline_btn_5 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
eseris_kb1 = InlineKeyboardMarkup(row_width=1).add(ontap_btn_1,ontap_btn_2,ontap_btn_3)

# конпки поддержки по работе с portfolio
port_btn_1 = InlineKeyboardButton('Преимущества ONTAP', callback_data='button1', url='https://app.gitbook.com/@anton-kyrylenko/s/tets/portfolio/untitled')
port_btn_2 = InlineKeyboardButton('FAS\AFF', callback_data='button2', url='https://app.gitbook.com/@anton-kyrylenko/s/tets/portfolio/netapp-fas-aff')
port_btn_3 = InlineKeyboardButton('E-series', callback_data='button3', url='https://app.gitbook.com/@anton-kyrylenko/s/tets/e-series')
#inline_btn_4 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
#inline_btn_5 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
port_kb1 = InlineKeyboardMarkup(row_width=1).add(ontap_btn_1,ontap_btn_2,ontap_btn_3)

# конпки поддержки по работе с design
#des_btn_1 = InlineKeyboardButton('Как бновить ПО', callback_data='button1', url='')
#des_btn_2 = InlineKeyboardButton('Обновить сертификат', callback_data='button2', url='')
#des_btn_3 = InlineKeyboardButton('Восстановить пароль', callback_data='button2', url='')
#inline_btn_4 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
#inline_btn_5 = InlineKeyboardButton('Открыть кейс', callback_data='button2', url='')
design_kb1 = InlineKeyboardMarkup(row_width=1).add(ontap_btn_1,ontap_btn_2,ontap_btn_3)
