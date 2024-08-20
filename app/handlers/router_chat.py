from aiogram import Router, F
from aiogram.types import Message, ChatPermissions
from aiogram.filters import Command, CommandObject
from aiogram.exceptions import TelegramBadRequest
from aiogram.enums.dice_emoji import DiceEmoji

from create_bot import bot
from filters.is_admin_chat import is_admin_chat
from utils.my_utils import parse_time

from contextlib import suppress


router = Router()
# Проверка, что сообщение отправлено не в приватном чате
router.message.filter(F.chat.type != "private")
# router.my_chat_member.filter(F.chat.type.in_({"group", "supergroup"}))


@router.message(Command('mute'), F.reply_to_message)
async def func_mute(message: Message, command: CommandObject):
    reply_message = message.reply_to_message

    if not await is_admin_chat(message, bot):
        await message.reply("<b>❌ Произошла ошибка!</b>")
        return
    date = parse_time(command.args)
    mention = reply_message.from_user.mention_html(reply_message.from_user.first_name)

    # with suppress(TelegramBadRequest):
    await bot.restrict_chat_member(chat_id=message.chat.id, 
                                        user_id=reply_message.from_user.id, 
                                        until_date=date, 
                                        permissions=ChatPermissions(can_send_messages=False))
    await message.reply(f"🔇 Пользователь <b>{mention}</b> был заглушен!")


@router.message(Command('unmute'), F.reply_to_message)
async def func_unmute(message: Message, command: CommandObject):
    reply_message = message.reply_to_message

    if not await is_admin_chat(message, bot):
        await message.reply("<b>❌ Произошла ошибка!</b>")
        return
    with suppress(TelegramBadRequest):
        await bot.restrict_chat_member(chat_id=message.chat.id, 
                                       user_id=reply_message.from_user.id, 
                                       permissions=ChatPermissions(can_send_messages=True))
        await message.reply("✅ Ограничения на чат сняты с пользователя!")


@router.message(Command("ban"), F.reply_to_message)
async def func_ban(message: Message, command: CommandObject):
    reply_message = message.reply_to_message

    if not await is_admin_chat(message, bot):
        await message.reply("<b>❌ Произошла ошибка!</b>")
        return
    date = parse_time(command.args)
    mention = reply_message.from_user.mention_html(reply_message.from_user.first_name)

    with suppress(TelegramBadRequest):
        await bot.ban_chat_member(chat_id=message.chat.id, user_id=reply_message.from_user.id, until_date=date)
        await message.reply(f"🚫 Пользователь <b>{mention}</b> был заблокирован!")


@router.message(Command("unban"))
async def func_unban(message: Message):
    reply_message = message.reply_to_message

    if not reply_message or not await is_admin_chat(message, bot):
        await message.reply("<b❌ Произошла ошибка!</b>")
        return
    with suppress(TelegramBadRequest):
        await bot.unban_chat_member(chat_id=message.chat.id, user_id=reply_message.from_user.id, only_if_banned=True)
        await message.reply("✅ Блокировка была снята")


help_text = "Вот справочник 📖\n\
1. '/mute' - для ограничения чата пользователю, чтобы указать с таймером: 1h, 1d, 1w\n\
2. '/unmute' - для снятия ограничения на чат пользователя\n\
3. '/ban' - для блокировки пользователя в группе, чтобы указать с таймером: 1h, 1d, 1w\n\
4. '/unban' - для снятия блокировски с пользователя \n\
5. '/dice' и '/basketball' - игры\n\n\
Команды используйте на сообщении пользователя"


@router.message(Command("help"))
async def help(message: Message):
    await message.answer(text=help_text)


@router.message(Command("dice"))
async def dice(message: Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)


@router.message(Command("basketball"))
async def basketball(message: Message):
    await message.answer_dice(emoji=DiceEmoji.BASKETBALL)


@router.message()
async def forbidden_words(message: Message):
    with open("forbidden_words.txt") as words:
        data = words.readlines()
        clean_data = [line.strip() for line in data]
    text = message.text.lower()
    text2 = message.text.lower().replace(' ', '')
    mention = message.from_user.mention_html(message.from_user.first_name)
    for word in clean_data:
        if word in text:
            await message.delete()
            await message.answer(text=f"{mention}, Такие слова запрещены!\nPS:Сообщение удалено.")
        if word in text2:
            await message.delete()
            await message.answer(text=f"{mention}, Такие слова запрещены!\nPS:Сообщение удалено.")
    if not await is_admin_chat(message, bot):
        for enity in message.entities:
            if enity.type in ['url', 'text_link']:
                await message.delete()
                await bot.send_message("Отправка ссылок - запрещена!\nДля получения разрешения на рекламу обратитесь к админу!")