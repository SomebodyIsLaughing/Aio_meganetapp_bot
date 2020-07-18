from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
import keyboards as kb
import hlp as hl

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_command_1(message: types.Message):
    await message.reply("В чем вопрос?", reply_markup=kb.inline_kb1)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(hl.help_message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
