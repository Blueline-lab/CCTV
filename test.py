import os 
import requests
import ID



def telegram_bot(bot_message):
        bot_token = ID.BOT_ID
        bot_chatID = ID.CHAT_ID
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + str(bot_message)

        response = requests.get(send_text)


telegram_bot("hello")