from aiogram import executor
from misc import dp, bot
import handlers
#слито в @smoke_software
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)