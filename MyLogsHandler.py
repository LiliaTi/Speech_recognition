import logging


class MyLogsHandler(logging.Handler):
    def __init__(self, tg_error_chat_id, bot):
        self.tg_error_chat_id = tg_error_chat_id
        self.bot = bot

    def emit(self, record):
        log_entry = self.format(record)
        self.bot.sendMessage(self.tg_error_chat_id, log_entry)
