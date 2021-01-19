import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
import os
import random
from dialogflow_functions import smart_answer
from telegram import Bot
import logging


LANGUAGE_CODE = "ru"


logger = logging.getLogger("VK Bot logger")


def vk_smart_answer(event, vk_api, project_id):
    answer = smart_answer(project_id=project_id, session_id=event.user_id,
                          text=event.text,
                          language_code=LANGUAGE_CODE)
    if not answer.intent.is_fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=answer.fulfillment_text,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    project_id = os.environ.get('PROJECT_ID')
    vk_token = os.environ.get('VK_TOKEN')

    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()

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

    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        try:
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                vk_smart_answer(event, vk_api, project_id)
        except Exception as e:
            logger.exception(e)

