from aiogram import types, Dispatcher

def register(dp: Dispatcher):
    @dp.message_handler(commands=["мотивация"])
    async def send_motivation(message: types.Message):
        await message.answer("Ты — боец. Ты идешь вперёд, даже когда больно. Can't hurt you.")