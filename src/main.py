from telegram import bot
from data.db import DataBase

if __name__ == '__main__':
    try:
        DataBase.get_connection()
        bot.main()
    except Exception as e:
        print('[Error] {e}')
    finally:
        DataBase.close_connection()
