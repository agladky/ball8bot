""" Bot to emulate ball 8. """

import logging
import config

from ball import Ball
from uuid import uuid4
from telegram.ext import (Updater, CommandHandler,
                          InlineQueryHandler, RegexHandler)
from telegram import (InlineQueryResultArticle, InputTextMessageContent,
                      ReplyKeyboardMarkup)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)
ball = Ball()


def start(bot, update):
    """
    Send a message when the command /start is issued.
    """
    reply_markup = ReplyKeyboardMarkup([['Потрясти 🎱']],
                                       resize_keyboard=True)
    update.message.reply_text('Выбирайте:', reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query
    bot.edit_message_text(text="Selected option: {}".format(query.data),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


def help(bot, update):
    """
    Send a message when the command /help is issued.
    """
    update.message.reply_text('Помошь')


def error(bot, update, error):
    """
    Log Errors caused by Updates.
    """
    logger.warning('Update "%s" caused error "%s"', update, error)


def shake(bot, update):
    """
    Emulation shaking of 8 ball. Send random answer.
    """
    update.message.reply_text(ball.shake())


def inline_shake(bot, update):
    """
    Emulation shaking of 8 ball. Send random answer inline.
    """
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title='Потрясти 🎱',
            input_message_content=InputTextMessageContent(ball.shake())
        ),
    ]
    update.inline_query.answer(results, cache_time=0)


def main():
    """
    Startup method.
    """
    updater = Updater(token=config.bot_token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('shake', shake))
    dispatcher.add_handler(RegexHandler('^Потрясти 🎱$', shake))

    dispatcher.add_error_handler(error)

    inline_caps_handler = InlineQueryHandler(inline_shake)
    dispatcher.add_handler(inline_caps_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
