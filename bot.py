from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import time
import threading

# Список пользователей для рассылки уведомлений
users = []

# Функция приветствия
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! I work 24/7 and will notify you as soon as new gifts become available!")
    # Добавляем пользователя в список
    if update.message.from_user.id not in users:
        users.append(update.message.from_user.id)

# Функция для отправки уведомлений о новых подарках
async def send11(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Sending notification to all users about new gifts...")
    # Отправляем уведомления всем пользователям
    await notify_users(context)

# Функция для отслеживания новых подарков
def check_for_new_gifts():
    # Эта функция будет проверять наличие новых подарков (например, через API Telegram)
    # Например, можно проверять сообщения на канале (это лишь пример, реальный мониторинг требует парсинга или API)
    new_gift_found = False  # Здесь должно быть условие для определения появления новых подарков
    
    # Псевдокод: если новый подарок найден
    if new_gift_found:
        notify_users()

# Функция уведомления пользователей (сделана асинхронной)
async def notify_users(context):
    for user_id in users:
        try:
            # Отправляем сообщение каждому пользователю
            await context.bot.send_message(user_id, "New gift available! Check it out!")
        except Exception as e:
            print(f"Error notifying user {user_id}: {e}")

# Функция для выполнения задачи раз в минуту
def job():
    while True:
        check_for_new_gifts()  # Проверяем на наличие новых подарков
        time.sleep(60)  # Задержка в 1 минуту (60 секунд)

# Основная функция для запуска бота
def main():
    # Ваш API Token
    application = Application.builder().token("7720837143:AAG3Qf-ho7ejkFcr7HWCJcrgL5I5tpMnSwY").build()

    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("send11", send11))

    # Запускаем планировщик в отдельном потоке
    threading.Thread(target=job).start()

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
