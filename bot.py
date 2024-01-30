from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Substitua 'SEU_TOKEN' pelo token do seu bot obtido do BotFather
TOKEN = '6932572671:AAFzVXSZ0GhkNSC99qGE4Wqzy1EC7j4wIVI'
SEU_ID_TELEGRAM = '5427353052'  # Substitua pelo seu ID Telegram

def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_name = update.message.from_user.username
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name

    response = f"Seu ID no Telegram é: {user_id}\n"
    response += f"Nome de usuário: @{user_name}\n"
    response += f"Seu Nome: {first_name}"

    if last_name:
        response += f" {last_name}"

    update.message.reply_text(response)

    # Encaminhar a mensagem para o seu ID Telegram
    context.bot.send_message(chat_id=SEU_ID_TELEGRAM, text=f'Mensagem enviada para o usuário:\n{response}')

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
