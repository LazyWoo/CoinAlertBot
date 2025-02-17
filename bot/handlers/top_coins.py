from aiogram import Router, types
from aiogram.filters import Command

from bot.crypto import CoinGeckoAPI


top_coins_router = Router()

crypto_api = CoinGeckoAPI()


@top_coins_router.message(Command("top_coins"))
async def top_coins(message: types.Message):
    top_100_coins = await crypto_api.get_top_100_coins()
    coins_message = "\n".join(f"{coin['name']} - {coin['current_price']} $USDT"  for coin in top_100_coins)

    await message.answer(coins_message)
