import logging
from typing import List

from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand

from bot.config import Config
from .handlers import all_routers


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot_log.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


dp = Dispatcher()

config = Config()


async def setup_routers(routers: List) -> None:
    for router in all_routers:
        try:
            dp.include_router(router)
            logging.info(f'Router [{router.name}] successfully connected.')
        except Exception as e:
            logging.error(f'Router [{router.name}] has been excepted: {e}')


async def start_bot() -> None:
    bot = Bot(token=config.bot_token)

    commands = [
        BotCommand(command="/start", description="Start bot"),
        BotCommand(command="/top_coins", description="Top coins"),
    ]
    await bot.set_my_commands(commands)

    await setup_routers(all_routers)

    try:
        logger.info("Bot is starting...")
        await dp.start_polling(bot)
    except Exception as e:
        logger.critical(f'Error occurred while starting the bot: {e}')
    finally:
        await bot.close()
        logger.info("Bot stopped.")
