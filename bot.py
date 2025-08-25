```python
import telebot
import os

TOKEN = os.getenv('TOKEN')  # Получаем токен из переменных окружения

bot = telebot.TeleBot(TOKEN)

user_states = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Напиши своё имя.")
    user_states[message.chat.id] = 'waiting_name'

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'waiting_name')
def check_name(message):
    name = message.text.strip()
    if name.lower() == 'алибек':
        bot.send_message(message.chat.id, "Ты гей 😎")
    else:
        bot.send_message(message.chat.id, "Ты не гей 🙃")
    user_states[message.chat.id] = None

bot.polling()
```