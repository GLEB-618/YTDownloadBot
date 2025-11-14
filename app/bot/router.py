from aiogram import Bot, Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, ReactionTypeEmoji, FSInputFile
from aiogram.enums.chat_type import ChatType
from app.core.logger import get_logger
from app.services.service import download_video
from app.services.utils import is_url, async_tempdir


router = Router()
logger = get_logger(__name__, "logs.log")


@router.message(F.text, F.chat.type == ChatType.PRIVATE)
async def search(msg: Message):
    url = msg.text

    if is_url(url):
        logger.info(f"Received message: {url} from user: {msg.from_user.id}")
        async with async_tempdir() as temp_dir:
            info = await download_video(url, temp_dir)

            file_path = info["filename"]
            format_note = info["format_note"]

            await msg.answer_video(video=FSInputFile(file_path), caption=f"Вот ваше видео с разрешением: {format_note}")    

            logger.info(f"Video sent to user: {msg.from_user.id}")
    else:
        await msg.answer("Пожалуйста, отправьте корректную ссылку.")
        logger.warning(f"Invalid URL received: {url} from user: {msg.from_user.id}")