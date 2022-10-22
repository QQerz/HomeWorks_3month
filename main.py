from aiogram.utils import executor
from config import bot, dp
import logging
from handlers import admin, callbak, client, extra, fsmAdminMentor


callbak.register_handlers_callback(dp)
client.register_handlers_client(dp)
fsmAdminMentor.register_handlers_fsm(dp)

extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
