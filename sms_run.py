import random
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
import telebot


url = "https://rest.nexmo.com/sms/json"
token = '509062716:AAHOJqcyC6igbvdqvjAa8QChs_6Ib3wDfgE'


# bot = telebot.TeleBot(token)
#
# @bot.message_handler(content_types=["text"])
def start_sending():
    sheduler = BlockingScheduler()
    sheduler.add_job(sms_send, 'interval', hours=1)
    sheduler.start()



def get_text():
    list_of_messages = ['Privet, gde moi trysu', "Sovest' delo tonkoe",
                        "Ded panas i ego dryzia idyt za toboy", "ti zabil zelenie tapochki", "KARIES...", "NO SMOKING!",
                        "NOT BAD, BUT BAD FOR YOU", "KAZDIY DEN' ODNO I TOZE" , "NET, eto ne shytka",
                        "davno bil y vracha?", "Y tebia ne bogatiy vnytrenniy mir", "pravosydie", "vezde est yshi",
                        ""]
    return list_of_messages[random.randint(0, len(list_of_messages))]

def get_data():

    data = {'api_key': '88e1d8c7',
            'api_secret': '081c53c18ce2fc8e',
            'to': '380637267402',
            'from': "Your conscience",
            'text': get_text()}

    return data

def get_headers():

    return {'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache"}

def sms_send():
    data = get_data()
    headers = get_headers()
    response = requests.request("POST", url, data=data, headers=headers)
    print(response.text)

if __name__ == '__main__':
    start_sending()
    # sheduler = BlockingScheduler()
    # sheduler.add_job(sms_send, 'interval', hours=1)
    # sheduler.start()