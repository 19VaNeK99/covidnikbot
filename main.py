import COVID19Py
import telebot

bot = telebot.TeleBot('1063682941:AAEHrQxRUxceL5BZ_RagAVY3e24OtUqAtiA')
covid = COVID19Py.COVID19()
latest = covid.getLatest()



@bot.message_handler(commands = ['start'])
def start(message):
    send_mess = f"<b> Привет {message.from_user.first_name}</b>\n Введите страну"
    bot.send_message(message.chat.id, send_mess, parse_mode = 'html')

@bot.message_handler(content_types = ['text'])
def mess(message):
    final_message  = ""
    get_message_bot = message.text.strip().lower()
    location = ""
    if get_message_bot == "сша":
        location = covid.getLocationByCountryCode("US")
    elif get_message_bot == "россия":
        location = covid.getLocationByCountryCode("RU")
    else:
        location = covid.getLatest()
        final_message = f"Данные по всему миру: \n Заболевшие :{location['confirmed']}"
    if final_message == "":
        date = location[0]['last_updated'].split('T')
        time = date[1].split(".")
        final_message = f"Данные по стране: \n Население {location[0]['country_population']} \n " \
                         + f"Заболевших {location[0]['latest']['confirmed']}"
    bot.send_message(message.chat.id, final_message, parse_mode="html")



bot.polling(none_stop = True)
