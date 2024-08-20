from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards.inline import add_bot

private_router = Router()
private_router.message.filter(F.chat.type == "private")

hello_text = 'Добро пожаловать! 👋 \n\nЯ бот Модератор для вашего чата. 🤖\n\nЕсли вы администратор группы:\nВы можете добавить меня, нажав кнопку ниже.\
 \nУбедитесь, что вы добавили бота как АДМИНА с разрешением «Управление группой», чтобы он мог работать правильно!\n\nЕсли вам нужна помощь:\n\
Просто наберите и отправьте «help» в чате.\
\n\nРазработчик <b>@MikeInTech</b>'


@private_router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply(hello_text, reply_markup=add_bot())
