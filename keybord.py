from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_test = KeyboardButton('/тест')
button_help = KeyboardButton('/помощь')
button_film = KeyboardButton('/фильмы')
kb_klient = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_klient.add(button_test).add(button_help).add(button_film)

#button_otwet_0 = KeyboardButton('/Биографии')
#button_otwet_1 = KeyboardButton('Боевики')
#button_otwet_2 = KeyboardButton('Вестерны')
#button_otwet_3 = KeyboardButton('Военные')
#button_otwet_4 = KeyboardButton('Детективы')
#button_otwet_5 = KeyboardButton('Детские')
#button_otwet_6 = KeyboardButton('Документальные')
#button_otwet_7 = KeyboardButton('драмы')
#button_otwet_8 = KeyboardButton('Исторические')
#button_otwet_9 = KeyboardButton('Комедии')
#button_otwet_10 = KeyboardButton('Криминал')
#button_otwet_11 = KeyboardButton('Мелодрамы')
#button_otwet_12 = KeyboardButton('Мультфильмы')
#button_otwet_13 = KeyboardButton('Мюзиклы')
#button_otwet_14 = KeyboardButton('Приключения')
#button_otwet_15 = KeyboardButton('Семейные')
#button_otwet_16 = KeyboardButton('Cпортивные')
#button_otwet_17 = KeyboardButton('Триллеры')
#button_otwet_18 = KeyboardButton('Ужасы')
#button_otwet_19 = KeyboardButton('Фантастика')
#button_otwet_20 = KeyboardButton('Фэнтези')

#kb_qwestion_1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#kb_qwestion_1.add(button_otwet_0).row(button_otwet_1, button_otwet_2, button_otwet_3).add(button_otwet_4).row(button_otwet_5, button_otwet_6, button_otwet_7).add(button_otwet_8).row(button_otwet_9, button_otwet_10, button_otwet_11).add(button_otwet_12).row(button_otwet_13, button_otwet_14, button_otwet_15).add(button_otwet_16).row(button_otwet_17, button_otwet_18, button_otwet_19).add(button_otwet_20)


#button_output_w = KeyboardButton('женский')
#button_output_m = KeyboardButton('мужской')

#kb_qwestion_7 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#kb_qwestion_7.row(button_output_m, button_output_w)
button_4_1 = KeyboardButton('/флегматик')
button_4_2 = KeyboardButton('/сангвиник')
button_4_3 = KeyboardButton('/холерик')
button_4_4 = KeyboardButton('/меланхолик')
button_sprawka = KeyboardButton('/справка')
kb_qwestion_4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_qwestion_4.row(button_4_1, button_4_2).row(button_4_3, button_4_4).add(button_sprawka)

button_5_1 = KeyboardButton('/веселый')
button_5_2 = KeyboardButton('/грустный')
button_5_3 = KeyboardButton('/расслабленный')
button_5_4 = KeyboardButton('/подавленный')
button_5_5 = KeyboardButton('/взбодренный')
button_5_6 = KeyboardButton('/депрессивный')
kb_qwestion_5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_qwestion_5.row(button_5_1, button_5_2, button_5_3).row(button_5_4, button_5_5, button_5_6)

button_6_1 = KeyboardButton('/позитивные')
button_6_2 = KeyboardButton('/негативные')
button_6_3 = KeyboardButton('/будоражащие')
button_6_4 = KeyboardButton('/приятные')
button_6_5 = KeyboardButton('/депрессивные')
kb_qwestion_6 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_qwestion_6.row(button_6_1, button_6_2).row(button_6_3, button_6_4).add(button_6_5)

button_r = KeyboardButton('/start')
kb_restart = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_restart.add(button_r)