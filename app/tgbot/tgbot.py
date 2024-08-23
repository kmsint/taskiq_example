import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.infrastructure.scheduler.taskiq_broker import broker, redis_source
from app.tgbot.handlers.commands import commands_router
from config.config import settings

logger = logging.getLogger(__name__)


async def main():
    logger.info("Starting bot")

    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode(settings.bot.parse_mode))
    )
    dp = Dispatcher()

    logger.info("Including routers")
    dp.include_routers(commands_router)

    logger.info("Starting broker")
    await broker.startup()

    logger.info("Starting polling")
    await dp.start_polling(bot, redis_source=redis_source)
    await broker.shutdown()