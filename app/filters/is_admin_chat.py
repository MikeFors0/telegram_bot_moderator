from aiogram.enums.chat_member_status import ChatMemberStatus


async def is_admin_chat(message, bot):
    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
    bot = await bot.get_chat_member(message.chat.id, bot.id)
    if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR]:
        return False
    return True