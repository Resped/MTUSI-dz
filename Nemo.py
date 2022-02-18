from telebot import types
import telebot;
bot = telebot.TeleBot('5220605405:AAGN4mK0I4Qa-IeLaEGS1CtsUdBsizOeGGk');
films = ['Крёстный отец']
serials = ['Во все тяжкие']
#Команды
@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я бот который поможет сохрвнить нужные сериалы и фильмы ')

@bot.message_handler(commands = ['help'])
def help(message):
    bot.send_message(message.chat.id, 'Напишите "Фильм", чтобы добавить фильм к списку, напишите "Сериал" чтобы добавить ка сериалам.\n\n Наишите боту "Покажи фильмы/сериалы" чтобы увидеть свой список сериалов.\n Используй /start чтобы начать, напиши /deletefilm, /deleteserials чтобы удалить всё из списка ')

@bot.message_handler(commands = ['deletefilm'])
def deletefilm(message):
    films.clear();
    bot.send_message(message.chat.id, 'Список фильмов очищен')

@bot.message_handler(commands = ['deleteserials'])
def deleteserials(message):
    serials.clear();
    bot.send_message(message.chat.id, 'Список сериалов очищен')

#Ответ на текст 
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Фильм':
    	bot.send_message(message.from_user.id, "Название фильма?");
    	bot.register_next_step_handler(message, get_film);
    
    elif message.text.lower() == 'покажи фильмы':
        bot.send_message(message.from_user.id, "Все?");
        bot.register_next_step_handler(message, doun_film);
    elif  message.text.lower() == "сериал":
        bot.send_message(message.from_user.id, "Название сериала?");
        bot.register_next_step_handler(message, get_serials);
    elif message.text.lower() == 'покажи сериалы':
        bot.send_message(message.from_user.id, "Все?");
        bot.register_next_step_handler(message, doun_serials);
    elif message.text.lower() == 'gym':
        bot.send_message(message.from_user.id, "GYM" * 30);
    elif message.text.lower() == 'абоба':
        bot.send_message(message.from_user.id, "АБОБА UwU");
    else:
        bot.send_message(message.from_user.id, "я пока не знаю, что ты мне написал.")



def get_film(message):
	global films;
	films.append(message.text);
	bot.send_message(message.from_user.id, 'Фильм добавлен');
def doun_film(message):
    global films;
    if len(films) == 0:
        bot.send_message(message.from_user.id, "Список фильмов пуст(")
    else:
        for f in films:
            bot.send_message(message.from_user.id, f)

def get_serials(message):
    global serials;
    serials.append(message.text);
    bot.send_message(message.from_user.id, 'Сериал добавлен');
def doun_serials(message):
    global serials;
    if len(serials) == 0:
        bot.send_message(message.from_user.id, 'Список сериалов пуст(')
    else:
        for s in serials:
            bot.send_message(message.from_user.id, s)

bot.polling(none_stop=True, interval=0)
