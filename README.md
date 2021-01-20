# Чатботы технической поддержки

Данный проект реализует двух чатботов технической поддержки для vk.com и telegram для вымышленной фирмы "Игра глаголов". Боты отвечают на типичные вопросы пользователей, представленные в произвольной форме. Боты были обучены нейросетью посредством сервиса [DialogFlow](https://dialogflow.cloud.google.com/). Логи каждого бота отправляются в установленный чат телеграм.

## Как использовать 

Отправьте вопрос ([доступные вопросы](https://github.com/LiliaTi/Speech_recognition/blob/main/questions.json)) [телеграм боту](https://telegram.me/devman_tech_support_bot) или [группе vk](https://vk.com/im?media=&sel=-201843313)

## Пример использования

Telegram
![](C:\Images\tg_bot_gif.gif)

VK
![](C:\Images\vk_bot_gif.gif)

## Как установить

### На локальной машине

Создайте в корне директории файл .env со следующими переменными
```python
PROJECT_ID="Your dialogflow project id"
GOOGLE_APPLICATION_CREDENTIALS="path to google credentials json file"
TG_ERROR_CHAT_ID='your chat_id for errors'
TG_BOT_TOKEN="Telegram bot token"
VK_TOKEN="Your vk group token" 
```

Создайте [DialogFlow project](https://cloud.google.com/dialogflow/es/docs/quick/setup), затем создайте [агента](https://cloud.google.com/dialogflow/es/docs/quick/build-agent) Запишите интенты и ответы для будущих ботов. Интенты также могут быть созданы скриптом `training.py`, он обучит сеть на примерах из `questions.json` 

Создайте [google credentials json file](https://cloud.google.com/docs/authentication/getting-started)

Создайте группу vk, в вашей группе кликните Управление -> Работа с API -> Создать ключ (разрешите отправку сообщений)

Создайте бота телеграм с помощью [@BotFather](https://telegram.me/botfather). Получите токен вашего бота

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:

```python
pip install -r requirements.txt
```
Запустите скрипты следующими командами:
```python
python vk_bot.py
```
```python
python tg_bot.py
```

### Деплой на Heroku

Склонируйте репозиторий, войдите или зарегистрируйтесь на [Heroku](https://dashboard.heroku.com)

Создайте новое приложение Heroku, во вкладке Deploy подключите ваш github аккаунт.Выберите нужный репозиторий.

Во вкладке Settings установите переменные окружения как Config Vars, [добавьте google credentials](https://stackoverflow.com/questions/47446480/how-to-use-google-api-credentials-json-on-heroku), используйте [этот билдпак](https://github.com/gerywahyunugraha/heroku-google-application-credentials-buildpack)

Активируйте бота на вкладке Resourses




