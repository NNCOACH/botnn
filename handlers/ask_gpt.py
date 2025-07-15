from aiogram import types, Dispatcher
from utils.openai_client import ask_gpt

def register(dp: Dispatcher):
    @dp.message_handler(commands=["ответ"])
    async def gpt_reply(message: types.Message):
        user_input = message.get_args()
        if not user_input:
            await message.reply("Напиши вопрос после команды /ответ")
            return
        reply = ask_gpt(user_input)
        await message.reply(reply)