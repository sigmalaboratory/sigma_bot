import tracemalloc
import emoji
import bec_
from bd_bec import *
from bec_ import *
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keybord import *

token_ = '5535371336:AAHiDYbg2tlixX2Yz_sEjHOgLu6JqoP_eVo'

tracemalloc.start()

bot = Bot(token=token_)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Start')


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer('Привет! Готовы выбирать фильм?', reply_markup=kb_klient)
    await message.delete()
    bec_.restart()


@dp.message_handler(commands=['помощь'])
async def command_help(message: types.Message):
    await message.answer('Привет, нужна помощ?')
    await message.answer('Sigma_Bot с невероятным количеством фильмов и сериалов. На котором всегда можно найти что-то свежее и интересное. Сама фишка бота, заключается в выборе фильмов по своему типу характера, а так же, настроению! Бот Вам подскажет кучу альтернативных вариантов, от самых новых и популярных, до старой классики - Комедий, блокбастеров, детективов, ужасов и прочее. Всегда готов помочь!')
    await message.answer(emoji.emojize('Есть вопросы, пиши нам :e-mail:sigmalaba@gmail.com'), reply_markup=kb_restart)
    await message.delete()


@dp.message_handler(commands=['фильмы'])
async def command_test(message: types.Message):
    await message.answer('https://t.me/cinema_sigma', reply_markup=kb_restart)
    await message.delete()



@dp.message_handler(commands=['тест'])
async def command_test(message: types.Message):
    await message.answer('Ваш тип характера?', reply_markup=kb_qwestion_4)
    await message.delete()
    await message.answer('Если вы не знаете ваш тип характера, воспользуйтесь справкой!')


@dp.message_handler(commands=['флегматик'])
async def qwestion_4_1(message: types.Message):
    await message.delete()
    three('Флегматик')
    await message.answer('Ваше эмоциональное состояние?', reply_markup=kb_qwestion_5)


@dp.message_handler(commands=['сангвиник'])
async def qwestion_4_2(message: types.Message):
    await message.delete()
    three('Сангвиник')
    await message.answer('Ваше эмоциональное состояние?', reply_markup=kb_qwestion_5)


@dp.message_handler(commands=['холерик'])
async def qwestion_4_3(message: types.Message):
    await message.delete()
    three('Холерик')
    await message.answer('Ваше эмоциональное состояние?', reply_markup=kb_qwestion_5)


@dp.message_handler(commands=['меланхолик'])
async def qwestion_4_4(message: types.Message):
    await message.delete()
    three('Меланхолик')
    await message.answer('Ваше эмоциональное состояние?', reply_markup=kb_qwestion_5)


@dp.message_handler(commands=['справка'])
async def qwestion_4_5(message: types.Message):
    await message.delete()
    await message.answer('Флегматик \nТакие люди неспешны, свои действия тщательно продумывают, все делают медленно и терпеть не могут суеты и спешки. Флегматики ответственны, старательны, вдумчивы, прилежны, настойчивы, миролюбивы, медлительны, прагматичны.')
    await message.answer('Сангвиник \nЭто крайне непоседливые, энергичные, легкие на подъем люди, которые очень любят движение')
    await message.answer('Холерик \nХолерики вспыльчивы, непостоянны, агрессивны и импульсивны. Несмотря на все вышесказанное, холерики, как правило, незлопамятны и очень отходчивы.')
    await message.answer('Меланхолик \nДостаточно ранимые, обидчивые и скрытые личности. Они склонны к глубоким переживаниям и грустным мыслям.', reply_markup=kb_qwestion_4)


@dp.message_handler(commands=['веселый'])
async def qwestion_5_1(message: types.Message):
    await message.delete()
    fhor('Веселые')
    await message.answer('Какие эмоции ожидаете от фильма?', reply_markup=kb_qwestion_6)


@dp.message_handler(commands=['грустный'])
async def qwestion_5_2(message: types.Message):
    await message.delete()
    fhor('Грустные')
    await message.answer('Какие эмоции ожидаете от фильма?', reply_markup=kb_qwestion_6)


@dp.message_handler(commands=['расслабленный'])
async def qwestion_5_3(message: types.Message):
    await message.delete()
    fhor('Рослаблены')
    await message.answer('Какие эмоции ожидаете от фильма?', reply_markup=kb_qwestion_6)


@dp.message_handler(commands=['подавленный'])
async def qwestion_5_4(message: types.Message):
    await message.delete()
    fhor('Подавлены')
    await message.answer('Какие эмоции ожидаете от фильма?', reply_markup=kb_qwestion_6)


@dp.message_handler(commands=['взбодренный'])
async def qwestion_5_5(message: types.Message):
    await message.delete()
    fhor('Взбодренны')
    await message.answer('Какие эмоции ожидаете от фильма?', reply_markup=kb_qwestion_6)


@dp.message_handler(commands=['депрессивный'])
async def qwestion_5_6(message: types.Message):
    await message.delete()
    fhor('Депресивны')
    await message.answer('Какие эмоции ожидаете от фильма?', reply_markup=kb_qwestion_6)


@dp.message_handler(commands=['позитивные'])
async def qwestion_6_1(message: types.Message):
    await message.delete()
    await message.answer('Приятного просмотра!')
    six('Позетивные')
    alfa = bd_bec.Search(bec_.lst)
    bd_bec.final(alfa)
    for item in bd_bec.lst_demo:
        await message.answer(emoji.emojize(':movie_camera:' + item), reply_markup=kb_restart)
        break


@dp.message_handler(commands=['негативные'])
async def qwestion_6_2(message: types.Message):
    await message.delete()
    await message.answer('Приятного просмотра!')
    six('Негативные')
    alfa = bd_bec.Search(bec_.lst)
    bd_bec.final(alfa)
    for item in bd_bec.lst_demo:
        await message.answer(emoji.emojize(':movie_camera:' + item), reply_markup=kb_restart)
        break


@dp.message_handler(commands=['будоражащие'])
async def qwestion_6_3(message: types.Message):
    await message.delete()
    await message.answer('Приятного просмотра!')
    six('Будоражущие')
    alfa = bd_bec.Search(bec_.lst)
    bd_bec.final(alfa)
    for item in bd_bec.lst_demo:
        await message.answer(emoji.emojize(':movie_camera:' + item), reply_markup=kb_restart)
        break


@dp.message_handler(commands=['приятные'])
async def qwestion_6_4(message: types.Message):
    await message.delete()
    await message.answer('Приятного просмотра!')
    six('Приятные')
    alfa = bd_bec.Search(bec_.lst)
    bd_bec.final(alfa)
    for item in bd_bec.lst_demo:
        await message.answer(emoji.emojize(':movie_camera:' + item), reply_markup=kb_restart)
        break


@dp.message_handler(commands=['депрессивные'])
async def qwestion_6_5(message: types.Message):
    await message.delete()
    await message.answer('Приятного просмотра!')
    six('Депресивные')
    alfa = bd_bec.Search(bec_.lst)
    bd_bec.final(alfa)
    for item in bd_bec.lst_demo:
        await message.answer(emoji.emojize(':movie_camera:' + item), reply_markup=kb_restart)
        break


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
