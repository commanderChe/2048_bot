import telebot
from telebot import types
from random import *
bot = telebot.TeleBot('8023932980:AAHGpCeywC8AEwiXf2QjvfXRsRtbqGGYA1Y')
users={}
keyboard = types.InlineKeyboardMarkup()
keyboard.row(types.InlineKeyboardButton("↑", callback_data="up"))
keyboard.row(types.InlineKeyboardButton("←", callback_data="left"),
             types.InlineKeyboardButton("↓", callback_data="down"),
             types.InlineKeyboardButton("→", callback_data="right"))
def line(border, n, max):
  r=border[0]+(border[1]*max+border[2])*n
  r=r[:-1]+border[3]
  return r
def gets(data, n, max, ex):
  place=data['place']
  fs="{:"+str(max)+"d}"
  r="<code>Points: "+str(data['score'])+"\n"+line("╔═╦╗", n, max)+"\n"
  for i in range(n):
    for j in range(n):
      if place[i][j][0]==ex:
        r+="║"+" "*max
      else:
        r+="║"+fs.format(place[i][j][0])
    r+="║\n"
    if i<n-1:
      r+=line("╠═╬╣", n, max)+"\n"
  r+=line("╚═╩╝", n, max)+"</code>"
  return r
def isvalid(place):
  v=False
  for i in range(3):
    for j in range(3):
      if place[i][j]==[1]:
        v=True
  for i in range(2):
    for j in range(3):
      if place[i][j]==place[i+1][j]:
        v=True
  for i in range(3):
    for j in range(2):
      if place[i][j]==place[i][j+1]:
        v=True
  for i in range(3):
    for j in range(3):
      if place[i][j]==[128]:
        v=False
  return v
def nl(place):
  v=False
  for i in range(3):
    for j in range(3):
      if place[i][j]==[1]:
        v=True
  if not v:
    return
  while True:
    randi=randint(0, 2)
    randj=randint(0, 2)
    if place[randj][randi]==[1]:
      break
  place[randj][randi]=[2]
def init():
  place=[[1], [1], [1]], [[1], [1], [1]], [[1], [1], [1]]
  nl(place)
  nl(place)
  return place
def left(data):
  place=data['place']
  for i in range(3):
    if place[i][0]==[1]:
      place[i][0]=place[i][1]
      place[i][1]=[1]
    if place[i][1]==[1]:
      place[i][1]=place[i][2]
      place[i][2]=[1]
    if place[i][0]==[1]:
      place[i][0]=place[i][1]
      place[i][1]=[1]
    if place[i][0]==place[i][1]!=[1]:
      place[i][0][0]*=2
      data["score"]+=place[i][0][0]
      place[i][1]=place[i][2]
      place[i][2]=[1]
    if place[i][1]==place[i][2]!=[1]:
      place[i][1][0]*=2
      data["score"]+=place[i][1][0]
      place[i][2]=[1]
  nl(place)
def right(data):
  place=data['place']
  for i in range(3):
    if place[i][2]==[1]:
      place[i][2]=place[i][1]
      place[i][1]=place[i][0]
      place[i][0]=[1]
    if place[i][1]==[1]:
      place[i][1]=place[i][0]
      place[i][0]=[1]
    if place[i][2]==[1]:
      place[i][2]=place[i][1]
      place[i][1]=place[i][0]
      place[i][0]=[1]
    if place[i][2]==place[i][1]!=[1]:
      place[i][2][0]*=2
      data["score"]+=place[i][2][0]
      place[i][1]=place[i][0]
      place[i][0]=[1]
    if place[i][1]==place[i][0]!=[1]:
      place[i][1][0]*=2
      data["score"]+=place[i][1][0]
      place[i][0]=[1]
  nl(place)
def up(data):
  place=data['place']
  for i in range(3):
    if place[1][i]==[1]:
      place[1][i]=place[2][i]
      place[2][i]=[1]
    if place[0][i]==[1]:
      place[0][i]=place[1][i]
      place[1][i]=[1]
    if place[1][i]==[1]:
      place[1][i]=place[2][i]
      place[2][i]=[1]
    if place[0][i]==place[1][i]!=[1]:
      place[0][i][0]*=2
      data["score"]+=place[0][i][0]
      place[1][i]=place[2][i]
      place[2][i]=[1]
    if place[1][i]==place[2][i]!=[1]:
      place[1][i][0]*=2
      data["score"]+=place[1][i][0]
      place[2][i]=[1]
  nl(place)
def down(data):
  place=data['place']
  for i in range(3):
    if place[2][i]==[1]:
      place[2][i]=place[1][i]
      place[1][i]=[1]
    if place[1][i]==[1]:
      place[1][i]=place[0][i]
      place[0][i]=[1]
    if place[2][i]==[1]:
      place[2][i]=place[1][i]
      place[1][i]=[1]
    if place[1][i]==place[2][i]!=[1]:
      place[2][i][0]*=2
      data["score"]+=place[2][i][0]
      place[1][i]=place[0][i]
      place[0][i]=[1]
    if place[0][i]==place[1][i]!=[1]:
      place[1][i][0]*=2
      data["score"]+=place[1][i][0]
      place[0][i]=[1]
  nl(place)
@bot.message_handler(commands=["start"])
def start(message):
  bot.send_message(message.chat.id, 'Привет! Я твой бот для игры в mini 2048 в телеграме. Напиши /help, чтобы узнать какие команды есть в боте. Напиши /info, чтобы узнать правила игры.')
@bot.message_handler(commands=["help"])
def help(message):
  bot.send_message(message.chat.id, 'Список команд: \n /start - начало работы с ботом \n /help - список команд \n /play - начало игры в mini 2048 \n /info - правила игры')
@bot.message_handler(commands=["info"])
def info(message):
  bot.send_message(message.chat.id, 'Бот будет выводить на экран поле, а пользователь управлять, используя кнопки(вверх, вниз, влево, вправо). Числа будут от 2 до 64 и 9 ячеек поля. Игра заканчивается, когда все ячейки поля заполнены или максимальное число 64.')
@bot.message_handler(commands=["play"])
def play(message):
  place=init()
  data={'place': place, 'score' : 0}
  users[message.chat.id]=data
  bot.send_message(message.chat.id, gets(users[message.chat.id], 3, 4, 1), parse_mode='HTML', reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
  data=users[query.message.chat.id]
  if query.data=="down":
    down(data)
  elif query.data=="up":
    up(data)
  elif query.data=="left":
    left(data)
  elif query.data=="right":
    right(data)
  if isvalid(data['place']):
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id, text=gets(data, 3, 4, 1), parse_mode='HTML', reply_markup=keyboard)
  else:
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id, text=gets(data, 3, 4, 1) + "\n\nИгра завершена", parse_mode='HTML')
bot.infinity_polling()