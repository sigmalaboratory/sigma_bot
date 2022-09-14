#from bd_bec import *


#lst_genre = []
import bd_bec

lst = []
#lst_w = []
#lst_m = []





#def one(x):
    #if x == "Биографии":
        #lst.append(0)
    #elif x == "Боевики":
        #lst.append(1)
    #elif x == "Вестерны":
        #lst.append(2)
   # elif x == "Военные":
    #    lst.append(3)
    #elif x == "Детективы":
     #   lst.append(4)
    #elif x == "Детские":
     #   lst.append(5)
    #elif x == "Документальные":
     #   lst.append(6)
    #elif x == "Драмы":
     #   lst.append(7)
    #elif x == "Исторические":
     #   lst.append(8)
    #elif x == "Комедии":
     #   lst.append(9)
    #elif x == "Криминал":
     #   lst.append(10)
   # elif x == "Мелодрамы":
    #    lst.append(11)
    #elif x == "Мультфильмы":
    #    lst.append(12)
    #elif x == "Мюзиклы":
     #   lst.append(13)
    #elif x == "Приключения":
     #   lst.append(14)
   # elif x == "Семейные":
    #    lst.append(15)
    #elif x == "Cпортивные":
     #   lst.append(16)
    #elif x == "Триллеры":
     #   lst.append(17)
    #elif x == "Ужасы":
     #   lst.append(18)
   # elif x == "Фантастика":
    #    lst.append(19)
    #elif x == "Фэнтези":
     #   lst.append(20)




#def two(x):
 #   if x == "Музыка":
  #      lst.append(0)
  #      lst.append(6)
   #   lst.append(9)
    #    lst.append(13)
    #elif x == "Искуство":
     #   lst.append(0)
      #  lst.append(6)
     #  lst.append(11)
      #  lst.append(13)
   # elif x == "Спорт":
    #    lst.append(0)
     #   lst.append(1)
      #  lst.append(9)
       # lst.append(14)
       # lst.append(16)
       # lst.append(18)
      #  lst.append(17)
    #elif x == "Компютерные игры":
     #   lst.append(14)
      #  lst.append(17)
       # lst.append(18)
       # lst.append(19)
       # lst.append(20)
    #elif x == "Наука":
     #   lst.append(0)
      #  lst.append(4)
       # lst.append(6)
        #lst.append(8)
      #  lst.append(19)
   # elif x == "Политика":
    #    lst.append(0)
     #   lst.append(3)
      #  lst.append(6)
       # lst.append(8)
   # elif x == "Предпренимательство":
    #    lst.append(10)
     #   lst.append(17)
   # elif x == "Извесные люди":
    #    lst.append(0)
     #   lst.append(6)
      #  lst.append(8)
   # elif x == "История":
    #    lst.append(0)
     #   lst.append(6)
      #  lst.append(8)
       # lst.append(3)
    #elif x == "Технологии":
     #   lst.append(20)
   # elif x == "Военное искуство":
    #    lst.append(3)
     #   lst.append(8)
    #else:
     #   return None

def three(x):
    if x == "Флегматик":
        lst.append(4)
        lst.append(6)
        lst.append(8)
        lst.append(10)
        lst.append(17)
    elif x == "Сангвиник":
        lst.append(1)
        lst.append(2)
        lst.append(9)
        lst.append(10)
        lst.append(14)
        lst.append(16)
        lst.append(17)
        lst.append(18)
        lst.append(19)
        lst.append(20)
    elif x == "Холерик":
        lst.append(1)
        lst.append(2)
        lst.append(3)
        lst.append(9)
        lst.append(10)
        lst.append(16)
        lst.append(17)
        lst.append(18)
        lst.append(19)
        lst.append(20)
        lst.append(14)
    elif x == "Меланхолик":
        lst.append(7)
        lst.append(11)
        lst.append(12)
        lst.append(13)
        lst.append(15)
    else:
        return None

def fhor(x):
    if x == "Веселые":
        lst.append(2)
        lst.append(9)
        lst.append(14)
    elif x == "Грустные":
        lst.append(7)
        lst.append(11)
    elif x == "Рослаблены":
        lst.append(9)
        lst.append(12)
        lst.append(13)
        lst.append(14)
        lst.append(15)
        lst.append(16)
    elif x == "Подавлены":
        lst.append(9)
        lst.append(13)
        lst.append(14)
        lst.append(15)
        lst.append(16)
        lst.append(17)
        lst.append(18)
    elif x == "Взбодренны":
        lst.append(4)
        lst.append(9)
        lst.append(14)
        lst.append(17)
        lst.append(18)
    elif x == "Депресивны":
        lst.append(7)
        lst.append(11)
    else:
        return None
#def five(x):
 #   if (x >= 0) and (x <= 12):
  #      lst.append(5)
   #     lst.append(12)
    #    lst.append(15)
    #elif (x >= 13) and (x <= 18):
     #   lst.append(1)
      #  lst.append(7)
       # lst.append(9)
        #lst.append(11)
      #  lst.append(12)
       # lst.append(13)
        #lst.append(14)
    #    lst.append(15)
     #   lst.append(16)
      #  lst.append(17)
       # lst.append(18)
        #lst.append(19)
     #   lst.append(20)
    #elif (x >= 18) and (x <= 26):
     #   for i in range(21):
      #      if i != 5:
       #         lst.append(i)
        #    else:
         #       continue
    #elif (x >= 27) and (x <= 35):
     #   for i in range(21):
      #      if (i != 5) and (i != 12) and (i != 18) and (i != 20):
       #         lst.append(i)
        #    else:
         #       continue
    #elif (x >= 36) and (x <= 45):
     #   for i in range(21):
      #      if (i != 5) and (i != 12) and (i != 18) and (i != 20):
       #        lst.append(i)
        #    else:
         #       continue
    #elif (x >= 46) and (x <= 100):
     #   lst.append(0)
      # lst.append(4)
      #  lst.append(6)
       # lst.append(7)
        #lst.append(8)
       # lst.append(10)
       # lst.append(15)
    #else:
     #   return None



def six(x):
    if x == "Позетивные":
        lst.append(9)
        lst.append(14)
        lst.append(15)
        lst.append(16)
        lst.append(19)
        lst.append(20)
    elif x == "Негативные":
        lst.append(3)
        lst.append(17)
        lst.append(18)
    elif x == "Будоражущие":
        lst.append(1)
        lst.append(2)
        lst.append(4)
        lst.append(10)
        lst.append(17)
        lst.append(18)
    elif x == "Приятные":
        lst.append(9)
        lst.append(12)
        lst.append(13)
        lst.append(14)
        lst.append(15)
        lst.append(16)
        lst.append(19)
        lst.append(20)
    elif x == "Депресивные":
        lst.append(3)
        lst.append(7)
        lst.append(11)
    else:
        return None
#def seven(x):
#    if x == "женский":
 #       for i in lst:
  #          if i != 1 and i != 2 and i != 3 and i != 5 and i != 12 and i != 17 and i != 18:
   #             lst_w.append(i)
    #           continue
     #   search = Search(lst_w)
      #  final(search)
   # if x == "мужской":
    #    for i in lst:
     #       if i != 5 and i != 7 and i != 11 and i != 12 and i != 13:
      #          lst_m.append(i)
       #     else:
        #        continue
        #search = Search(lst_m)
        #final(search)

def restart():
    lst.clear()
    bd_bec.lst_demo.clear()

