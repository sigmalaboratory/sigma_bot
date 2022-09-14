from collections import Counter
import sqlite3
from random import randint

lst_demo = []


def serch_bd(x):
    db = sqlite3.connect('sigma.db')
    cursor = db.cursor()
    cursor.execute("SELECT title FROM films WHERE genre = ?", x)
    title = cursor.fetchall()
    bd_namber = len(title)
    number = randint(1, bd_namber - 1)
    finish = title[number]
    for item in finish:
        lst_demo.append(item.lstrip())



def Search(lst):
    return dict(Counter(lst))

def final(dict_):
    lst = []
    lst_final =[]
    max_val = max(dict_.values())
    final_dict = {k: v for k, v in dict_.items() if v == max_val}
    for i in final_dict:
        lst.append(i)


    for j in lst:
        if j == 0:
            lst_final.append("Биографии")
        elif j == 1:
            lst_final.append("Боевики")
        elif j == 2:
            lst_final.append("Вестерны")
        elif j == 3:
            lst_final.append("Военные")
        elif j == 4:
            lst_final.append("Детективы")
        elif j == 5:
            lst_final.append("Детские")
        elif j == 6:
            lst_final.append("Документальные")
        elif j == 7:
            lst_final.append("Драмы")
        elif j == 8:
            lst_final.append("Исторические")
        elif j == 9:
            lst_final.append("Комедии")
        elif j == 10:
            lst_final.append("Криминал")
        elif j == 11:
            lst_final.append("Мелодрамы")
        elif j == 12:
            lst_final.append("Мультфильмы")
        elif j == 13:
            lst_final.append("Мюзиклы")
        elif j == 14:
            lst_final.append("Приключения")
        elif j == 15:
            lst_final.append("Семейные")
        elif j == 16:
            lst_final.append("Cпортивные")
        elif j == 17:
            lst_final.append("Триллеры")
        elif j == 18:
            lst_final.append("Ужасы")
        elif j == 19:
            lst_final.append("Фантастика")
        elif j == 20:
            lst_final.append("Фэнтези")
        else:
            return None
    demo_result = lst_final[0]
    result = [f' {demo_result} ']
    serch_bd(result)





