from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
import keyboards as kb
import help as hp


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Клавиатура - mysupport
@dp.message_handler(commands=['mysupport'])
async def process_command_1(message: types.Message):
    await message.reply("В чем вопрос? ", reply_markup=kb.inline_kb1)

# клавиатура ONTAP
@dp.message_handler(commands=['ontap_basic'])
async def process_command_2(message: types.Message):
    await message.reply("Лучшие категории, для лучших людей \U0001F60E", reply_markup=kb.ontap_kb1)

# Помощь
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(hp.help_message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
