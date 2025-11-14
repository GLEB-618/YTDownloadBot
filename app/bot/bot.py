from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from app.bot.router import router
from app.core.config import settings
from app.core.logger import get_logger

logger = get_logger(__name__, "logs.log")


async def run_bot():
    try:
        bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        dp = Dispatcher() 

        dp.include_routers(router)

        logger.info("Бот запущен")

        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Error: {e}")