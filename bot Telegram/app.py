#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import gspread
from datetime import datetime
import random
import telebot
import schedule

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep, time

import requests
from bs4 import BeautifulSoup as bs

#with open("conf.py", "w", encoding="utf-8") as f:
    #f.write('TOKEN = "%s"' %
            #input("5375722654:AAHwz7Tm1bSPy-S0F7tOJDVbzVyXcW5TWeI"))
        
def edit_year(date):
    if len(date) < 10:
        date += '.1980'
    return date


def date_time(x):
    date = datetime.strptime(x, "%d.%m.%Y")
    return date


def edit_login(login):
    if login.startswith('@'):
        return login
    else:
        new_login = '@' + login
    return new_login

def create_gift():
    url = 'https://pozdravok.com/pozdravleniya/a/proza.htm'
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    driver.get(url)

    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    results = soup.find_all('p', class_='sfst')
    gifts = []
    for result in results:
        gifts.append(result.text)
    return random.choice(gifts)

pril = ['аппетитные', 'божественные', 'блестящие', 'благоуханные', 'бесценные', 'будоражащие', 'блистательные', 'бесподобные', 'великолепные', 'великие', 'волнительные', 'воздушные', 'властные', 'вдохновляющие', 'восхитительные', 'горячие', 'грациозные', 'дорогие', 'дивные', 'дражайшие', 'дикие', 'драгоценные', 'дикие', 'единственные', 'желанные', 'женственные', 'золотые', 'загадочные', 'изумительные', 'идеальные', 'креативные',
        'красивые', 'лучезарные', 'ласковые', 'любимые', 'милые', 'маленькие', 'нежные', 'небесные', 'ненаглядные', 'неповторимые', 'неотразимые', 'незабвенные', 'невероятные', 'неземные', 'обожаемые', 'окрыляющие', 'очаровательные', 'обворожительные', 'привлекательные', 'пленительные', 'родные', 'сладкие', 'сногсшибательные', 'сказочные', 'снежные', 'удивительные', 'фантастические', 'феерические', 'хорошие', 'шикарные', 'яхонтовые']
words = ['антилопы', 'амурчики', 'ананасики', 'апельсинки', 'афродиты', 'аистенки', 'ангелы', 'ангелочки', 'бусеньки', 'богини', 'бурундучки', 'барбариски', 'булочки', 'былинки', 'бельчонки', 'белочки', 'бриллиантики', 'бабочки', 'бублички', 'бестии', 'бусинки', 'вредины', 'вафельки', 'волшебницы', 'вишенки', 'вкусняшки', 'виноградинки', 'веснушки', 'ватрушечки', 'василки', 'голубки', 'горошинки', 'галчонки', 'гусенки', 'дорогуши', 'дюймовочки', 'душечки', 'детки', 'души', 'мои', 'дельфиненки', 'дикобразики', 'ежики', 'ежиньки', 'егозы', 'ежевички', 'жучки', 'жемчужины', 'золотца', 'забавы', 'зефирки', 'златовласки', 'звездочки', 'зайки', 'зайчики', 'зайчонки', 'зайчоныши', 'звеpеныши', 'землянички', 'изумрудики', 'искусительницы', 'искорки', 'ириски', 'игрульки', 'изюминки', 'киски', 'кошечки', 'котенки', 'кисульки', 'красотульки', 'козочки', 'колобки', 'капризульки', 'карапузики', 'козявочки', 'кнопки', 'котлетки', 'кнопочки', 'крохотульки', 'колючки', 'крокозябрики', 'карасики', 'красотки', 'кошечки', 'кукушонки', 'круассанчики', 'куксики', 'кровиночки', 'кролики', 'кролички', 'крошки', 'конфетки', 'клубнички', 'клюковки', 'карамельки', 'красавицы', 'курочки', 'куколки', 'кудряшки', 'кускусики', 'лютики', 'лебедушки', 'лапочки', 'лучики', 'лапушки', 'лапули', 'ляли', 'лялечки', 'лапки', 'львенки', 'лимпопоши', 'лепесточки', 'ласточки', 'льдинки', 'лимончики', 'лисенки', 'лани', 'ласкуши', 'ласточки', 'лягушонки', 'малыши',
         'малышки', 'мурлыки', 'малютки', 'малявочки', 'мальвинки', 'мармеладки', 'медвежонки', 'малышки', 'мурзеныши', 'мяфмяфочки', 'мисюси', 'мушки', 'мечты', 'морковки', 'мумитролльчики', 'малинки', 'мусики', 'мурзилки', 'мышонки', 'мимишечки', 'незабудки', 'няши', 'нямочки', 'обаяшки', 'очаровашки', 'осинки', 'облачки', 'олененки', 'одуванчики', 'обольстительницы', 'огонки', 'персики', 'птенчики', 'пташки', 'пушинки', 'поросеночки', 'пупсики', 'пупсеныши', 'печеньки', 'проказницы', 'прелести', 'пельмешки', 'плюшечки', 'пампушечки', 'пончики', 'поночки', 'перчики', 'пусики', 'пятачки', 'пингвинчики', 'пузатики', 'полосатики', 'паровозики', 'половинки', 'пушистики', 'пушки', 'пpелестницы', 'пампушечки', 'пухляши', 'пухлики', 'розочки', 'ромашки', 'рыбки', 'рыжики', 'рыжечки', 'рыжульки', 'радости', 'роднульки', 'рысенки', 'солнышки', 'сердечки', 'сердцеедки', 'слапопуськи', 'слоненки', 'синички', 'соблазнительницы', 'сахарки', 'снежки', 'светлячки', 'совенки', 'симпатяжки', 'смородинки', 'снежинки', 'снегирки', 'снежки', 'сокровища', 'тигренки', 'тигрульки', 'тыковки', 'телепузики', 'тростинки', 'тефтельки', 'услады', 'усипуськи', 'ушастики', 'умницы', 'утенки', 'умки', 'фунтики', 'финтифлюшки', 'хитрюгы', 'хомячки', 'херувимчики', 'цветочки', 'цветик-семицветики', 'цыпленки', 'чуди', 'чебурашки', 'чеpтенки', 'черешенки', 'шалунишки', 'шоколадки', 'щекастики', 'эклерчики', 'ягодки', 'ясноглазки', 'яблочки', 'пушистики']

bot = telebot.TeleBot('5375722654:AAHwz7Tm1bSPy-S0F7tOJDVbzVyXcW5TWeI')

@bot.message_handler(commands=['start'])
def main_func(message):
    # подключаем файл с ключами и пр.
    gs = gspread.service_account(filename='bothb_key.json')
    # подключаем таблицу по ID
    sh = gs.open_by_key('1xzpuCyE7bYKDBRtVRKNK--DxVX0T1F2uRLTAvCUAiG8')
    worksheet = sh.sheet1  # получаем первый лист

    values = worksheet.get_all_values()
    columns = values[0]
    data = pd.DataFrame(values[1:], columns=columns)

    data['День рождения'] = data['День рождения'].apply(lambda x: edit_year(x))
    data['День рождения'] = data['День рождения'].apply(lambda x: date_time(x))
    data['день'] = data['День рождения'].apply(lambda x: x.day)
    data['месяц'] = data['День рождения'].apply(lambda x: x.month)
    data['Ник в Telegram'] = data['Ник в Telegram'].apply(
        lambda x: edit_login(x))

    current_datetime = datetime.now()
    birthday_data = data[(data['день'] == current_datetime.day) & (
        data['месяц'] == current_datetime.month)]
    if len(birthday_data) != 0:
        for i in range(len(birthday_data)):
            greeting = 'Сегодня у нас есть именинник! ' + birthday_data.iloc[i]['Имя'] + ' ' + birthday_data.iloc[i]['Ник в Telegram']                + '\n' + create_gift()
        bot.send_message(message.chat.id, greeting)
    else:
        greeting = "Доброе утро, " + random.choice(pril) + ' ' + random.choice(words) +'! \n Хорошего вам дня!'
        bot.send_message(message.chat.id, greeting)

#schedule.every().day.at('07:00').do(main_func)

bot.polling(none_stop=True)

