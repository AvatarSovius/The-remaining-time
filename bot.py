import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

logging.info('''==========================''')


def start_message(bot, update):
    text = 'Есть одно важное условие радостной жизни — всегда помнить, что она закончится'
    text_2 = '''
    Не ждите, когда закончите институт, когда родятся дети. Хватит ждать, когда начнете работать, когда уйдете на пенсию, когда женитесь, разведетесь. Не ждите вечера пятницы, утра воскресенья, покупки новой машины, новой квартиры. Не ждите весны, лета, осени, зимы. Минуты счастья — драгоценны, это не конечный пункт путешествия, а само путешествие. Работайте — не только ради денег, любите — не в ожидании расставаний. Танцуйте — не обращая внимания на взгляды. Самая ужасная ошибка, которую вы можете совершить — это всю жизнь гнаться за целями, не замечая как мимо вас пробегает ваша жизнь…
    '''
    text_3 = 'Хочешь узнать, сколько тебе осталось жить на этой планете в часах, днях, минутах?\nВводи комманду /life пол возраст\nПример: /life М 30'
    logging.info('Вызван /start')
    update.message.reply_text(text)
    update.message.reply_text(text_2)
    update.message.reply_text(text_3)


def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info(
        "User: {}, Chat id: {}, Message {}".format(update.message.chat.username, update.message.chat.id,
                                                   update.message.text))
    update.message.reply_text(user_text)


def get_sum_life(bot, update):
    text = update.message.text.split(' ')
    man = 582540
    lady = 657000

    if text[1].lower() == 'м':
        score = man - ((int(text[2]) * 365) * 24)
        score_days = (lady / 24) - int(text[2]) * 365
        update.message.reply_text(
            'Тебе осталось жить: {} часов.\nДней: {}\nТы  '.format(score, score_days))
    else:
        score = lady - ((int(text[2]) * 365) * 24)
        score_days = (lady / 24) - int(text[2]) * 365
        update.message.reply_text(
            'Тебе осталось жить: {} часов.\nДней: {} '.format(score, score_days))


def main():
    mybot = Updater(settings.TELEGRAM_TOKEN)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", start_message))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("life", get_sum_life))

    mybot.start_polling()
    mybot.idle()


main()
