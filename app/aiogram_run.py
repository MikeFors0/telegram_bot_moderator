import asyncio
from create_bot import bot, dp
from handlers.router_chat import router
from handlers.private import private_router
import logging
from contextlib import suppress


async def main():
    dp.include_router(router)
    dp.include_router(private_router)
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        logging.error(f"[!!! Exception] - {e}", exc_info=True)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    with suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(main())