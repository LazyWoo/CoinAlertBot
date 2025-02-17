from aiogram import Router, types
from aiogram.filters import CommandStart


start_router = Router()


@start_router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Hello! 🚀 Stay updated with the latest crypto info. Let's get started!")
