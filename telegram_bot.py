# A small example on how to send an autamated message using a telegram bot.

# Author: Faisal Ali
# Creation Date: 02-Dec-2020
# Version: 1.0

# Importing libraries
import logging
import telegram

# Function for sending message
def send_telegram_notification(msg):
    try:
        logger.info(f"--- Telegram Message --- {msg} ---") # Logging the status
        bot_token = "" # Add the token of your bot here
        userchat_id = "" # Add user or group chat id here
        bot = telegram.Bot(token = bot_token) # Initialize the bot
        bot.send_message(chat_id = userchat_id, text = msg) # Send the message
        logger.info("--- Telegram Message --- Sent ---")

    except Exception as error:
        logger.info(f"--- Telegram Message --- Failed --- {error} ---")

def main():
    msg = "This is our first test message"
    send_telegram_notification(msg)

if __name__ == "__main__":
    logging.basicConfig(filename = 'bot.log', level=logging.INFO, format='%(asctime)s -> %(message)s') # Configuration for logging
    logger = logging.getLogger()
    main()