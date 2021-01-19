from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import logging
from dialogflow_functions import smart_answer


LANGUAGE_CODE = "ru"

logger = logging.getLogger("TG Bot logger")


def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Здравствуйте!")


def tg_smart_answer(update, context):
    chat_id = update.effective_chat.id
    answer = smart_answer(project_id=os.environ.get('PROJECT_ID'), session_id=chat_id,
                          text=update.message.text,
                          language_code=LANGUAGE_CODE)
    context.bot.send_message(chat_id=chat_id, text=answer.fulfillment_text)


def main():
    tg_bot_token = os.environ.get('TG_BOT_TOKEN')
    tg_error_chat_id = os.environ.get('TG_ERROR_CHAT_ID')

    bot = Bot(tg_bot_token)
    class MyLogsHandler(logging.Handler):

        def emit(self, record):
            log_entry = self.format(record)
            bot.sendMessage(tg_error_chat_id, log_entry)

    logging.basicConfig(format="%(process)d %(levelname)s %(message)s")
    logger.setLevel(logging.INFO)
    logger.addHandler(MyLogsHandler())

    try:
        updater = Updater(tg_bot_token, use_context=True)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(MessageHandler(
            Filters.text & ~Filters.command, tg_smart_answer))
    except Exception as e:
        logger.exception(e)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
