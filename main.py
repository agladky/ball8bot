""" Bot to emulate ball 8. """

import logging
import gettext
import random
from uuid import uuid4
from telegram.ext import (
    Updater,
    CommandHandler,
    InlineQueryHandler,
    MessageHandler,
    Filters,
)
from telegram import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    ReplyKeyboardMarkup,
)
import config


SUPPORTED_LANGUAGES = ["en", "ru"]
languages = (
    [config.language]
    if config.language in SUPPORTED_LANGUAGES
    else [SUPPORTED_LANGUAGES[0]]
)
translation = gettext.translation("base", localedir="locale", languages=languages)
_ = translation.gettext

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

answers = (
    _("It is certain"),
    _("It is decidedly so"),
    _("Without a doubt"),
    _("Yes - definitely"),
    _("You may rely on it"),
    _("As I see it, yes"),
    _("Most likely"),
    _("Outlook good"),
    _("Yes"),
    _("Signs point to yes"),
    _("Reply hazy, try again"),
    _("Ask again later"),
    _("Better not tell you now"),
    _("Cannot predict now"),
    _("Concentrate and ask again"),
    _("Don't count on it"),
    _("My reply is no"),
    _("My sources say no"),
    _("Outlook not so good"),
    _("Very doubtful"),
)


def start(update, context):
    """
    Send a message when the command /start is issued.
    """
    reply_markup = ReplyKeyboardMarkup([[_("Shake the 🎱")]], resize_keyboard=True)
    update.message.reply_text("{}:".format(_("Choose")), reply_markup=reply_markup)


def help(update, context):
    """
    Send a message when the command /help is issued.
    """
    update.message.reply_text(_("Help"))


def error(update, context):
    """
    Log Errors caused by Updates.
    """
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def shake(update, context):
    """
    Emulation shaking of 8 ball. Send random answer.
    """
    update.message.reply_text(random.choice(answers))


def inline_shake(update, context):
    """
    Emulation shaking of 8 ball. Send random answer inline.
    """
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title=_("Shake the 🎱"),
            input_message_content=InputTextMessageContent(random.choice(answers)),
        ),
    ]
    update.inline_query.answer(results, cache_time=0)


def main():
    """
    Startup method.
    """
    updater = Updater(token=config.bot_token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("shake", shake))
    dispatcher.add_handler(
        MessageHandler(Filters.regex("^{}$".format(_("Shake the 🎱"))), shake)
    )
    dispatcher.add_handler(InlineQueryHandler(inline_shake))
    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
