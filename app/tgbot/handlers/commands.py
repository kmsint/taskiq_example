from datetime import datetime, timedelta, timezone
from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from taskiq_redis import RedisScheduleSource
from app.infrastructure.scheduler.tasks import simple_task, scheduled_task, dynamic_periodic_task, broker

commands_router = Router()


@commands_router.message(CommandStart())
async def process_start_command(message: Message) -> None:
    await message.answer(
        text='Я бот, демонстрирующий работу с Taskiq. Доступны команды:\n\n'
             '/simple - Простая задача, которая начинает выполняться сразу\n'
             '/delay - Задача, которая начнет выполняться через 5 секунд\n'
             '/periodic - Динамически планируемая периодическая задача, будет выполняться раз в 2 минуты'
    )


@commands_router.message(Command('simple'))
async def task_handler(message: Message, redis_source: RedisScheduleSource):
    await simple_task.kiq()
    await message.answer('Простая задача')


@commands_router.message(Command('delay'))
async def delay_task_handler(message: Message, redis_source: RedisScheduleSource):
    await scheduled_task.schedule_by_time(
        source=redis_source, 
        time=datetime.now(timezone.utc) + timedelta(seconds=5)
    )
    await message.answer(text='Задача выполнится скоро')


@commands_router.message(Command('periodic'))
async def dynamic_periodic_task_handler(message: Message, redis_source: RedisScheduleSource):
    await dynamic_periodic_task.schedule_by_cron(
        source=redis_source, 
        cron='*/2 * * * *'
    )
    await message.answer(text='Это динамически планируемая периодическая задача')