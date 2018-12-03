import settings
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

logging.info('''==========================!''')
logging.info('Бот запущен!')

def start_message(bot, update):
    text = 'Добрый день, вы знаете что жизнь скоротечна? И откладывая все на завтра, вы  теряете частичку себя.'
    logging.info('Вызван /start')
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info(
        "User: {}, Chat id: {}, Message {}".format(update.message.chat.username, update.message.chat.id,
                                                   update.message.text))
    update.message.reply_text(user_text)


def get_sum_life(bot,update):
    text = update.message.text.split(' ')
    life_time = 569400
    print(text)
    your_time = (int(text[1]) * 365) * 24
    print(your_time)
    suming = life_time - your_time
    update.message.reply_text(suming)



def main():
    mybot = Updater(settings.TELEGRAM_TOKEN)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", start_message))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("life", get_sum_life))

    mybot.start_polling()
    mybot.idle()


main()
