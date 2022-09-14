import requests
from bs4 import BeautifulSoup
import lxml
from random import randint
import sqlite3
#r = input()
#x = [f' {r} ']
#lst_alpha = []
#lst_final = []
#lst = [['Слепая (1 сезон)', 'Драма'], ['Волчок (2009)', 'Драма'], ['Легенда о пианисте (1998)', 'Драма'], ['Фарго (1995)', 'Триллер'], ['Районы (2016)', 'Драма'],['Война Харта (2002)', 'Военный'], ['Стикер (2022)', 'Детектив'], ['72 метра (2004)', 'Драма'], ['Смерть на похоронах (2010)', ' Комедия'], ['Побег из Алькатраса (1979)', 'Драма']]
#db = sqlite3.connect('sigma.db')
#cursor = db.cursor()
#cursor.execute("""CREATE TABLE films (
        #title text,
        #genre text
#)""")

#cursor.execute("SELECT title FROM films WHERE genre = ?", x)
#cursor.execute("DELETE FROM films")
#bd = cursor.fetchall()
#bd_namber = len(bd)
#number = randint(1, bd_namber - 1)
#print(bd[number])
#print(cursor.fetchall())
#headers = {
    #'Accept': '*/*',
    #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
#}

#for i in range(1, 10):
    #url = f'https://rezka.ag/films/best/1995/page/{i}/'
    #req = requests.get(url, headers=headers)
    #src = req.text
    #soup = BeautifulSoup(src, 'lxml')
    #inf = soup.find_all(class_="b-content__inline_item-link")
    #for item in inf:
        #text = item.text
        #alpha = text.split(',')
        #index = len(alpha)
        #if index > 2:
           #lst_alpha.append([alpha[0], alpha[2]])
        #elif index <= 2:
            #lst_alpha.append([alpha[0], alpha[1]])
#print(lst_alpha)
#cursor.executemany("INSERT INTO films VALUES (?, ?)", lst_alpha)
#cursor.execute("SELECT * FROM films ")
#a = cursor.fetchall()
#print(a)
#print(len(a))
#db.commit()
#db.close()



