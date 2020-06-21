import time

import telebot
from telebot import types

token = "1192793418:AAFt0guHDc8qZLCVVpUM6OIPmWjcVGGlU74"
bot = telebot.TeleBot(token)
from base import SQLite

db = SQLite('database.db')
from categ import catergories
import vk_data


link = 'https://telegra.ph/CHto-takoe-fudshering-i-kak-ispolzovat-bota-06-20-2'


@bot.message_handler(commands=['start'])
def start(message):
    # Добавление пользователя в базу данных
    if (not db.user_exists(message.from_user.id)):  # Проверяем, есть ли в базе пользователь
        db.add_user(message.from_user.id)  # Если его нету - добавляем его в базу данных
    keyboardmain = types.InlineKeyboardMarkup(row_width=2)
    bot.send_message(message.chat.id,
                     f'Добро пожаловать, {message.from_user.username}!\n\nМеня зовут FoodSharingBot. Я помогаю '
                     f'улучшить фудшеринг в России.\n\nФудшеринг (от англ. food — «еда», sharе — «делиться») — это '
                     f'движение, участники которого бесплатно отдают или забирают себе еду. Как правило, речь идёт об '
                     f'излишках продуктов, иногда — с истекающим сроком годности. Но ни в коем случае не об объедках '
                     f'и не о чём-то испорченном.\n\nБолее подробно вы можете прочитать в нашей статье {link}')

    btn1 = types.InlineKeyboardButton(text="Новосибирск", callback_data="novosibirsk")
    #btn2 = types.InlineKeyboardButton(text="Москва", callback_data="moscow")
    keyboardmain.add(btn1)
    bot.send_message(message.chat.id,
                     "Выберите город:",
                     parse_mode='html',
                     reply_markup=keyboardmain)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "novosibirsk":
        db.update_city(call.from_user.id, "nsk")
        keyboard = types.InlineKeyboardMarkup()
        next = types.InlineKeyboardButton(text="Перейти к выбору категорий", callback_data="select-category")
        keyboard.add(next)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Теперь необходимо настроить категории.",
                              reply_markup=keyboard)

    if call.data == "moscow":
        db.update_city(call.from_user.id, "msk")
        keyboard = types.InlineKeyboardMarkup()
        next = types.InlineKeyboardButton(text="Перейти к выбору категорий", callback_data="select-category")
        keyboard.add(next)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Теперь необходимо настроить категории.",
                              reply_markup=keyboard)

    if call.data == "select-category":
        catergories(call)

    # =====НАСТРОЙКА КАЖДОЙ КАТЕГОРИИ ОТДЕЛЬНО=====
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-= МЯСО -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-
    if call.data == "meat":
        if (db.check(call.from_user.id, "meat") == "TRUE"):  # Проверяем если мясо включенно
            db.update(call.from_user.id, "FALSE", "meat")
            # обновляем
            catergories(call)
        else:
            db.update(call.from_user.id, "TRUE", "meat")
            # обновляем
            catergories(call)
    # -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-= РЫБА -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-
    if call.data == "fish":
        if (db.check(call.from_user.id, "fish") == "TRUE"):  # Проверяем если мясо включенно
            db.update(call.from_user.id, "FALSE", "fish")
            # обновляем
            catergories(call)
        else:
            db.update(call.from_user.id, "TRUE", "fish")
            # обновляем
            catergories(call)
    # -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-= МОЛОКО -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-
    if call.data == "milk":
        if (db.check(call.from_user.id, "milk") == "TRUE"):  # Проверяем если мясо включенно
            db.update(call.from_user.id, "FALSE", "milk")
            # обновляем
            catergories(call)
        else:
            db.update(call.from_user.id, "TRUE", "milk")
            # обновляем
            catergories(call)
    # -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-= НАПИТКИ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-
    if call.data == "drinks":
        if (db.check(call.from_user.id, "drinks") == "TRUE"):  # Проверяем если мясо включенно
            db.update(call.from_user.id, "FALSE", "drinks")
            # обновляем
            catergories(call)
        else:
            db.update(call.from_user.id, "TRUE", "drinks")
            # обновляем
            catergories(call)
    # -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-= ФРУКТЫ И ОВОЩИ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-
    if call.data == "fruitsandvegetables":
        if (db.check(call.from_user.id, "fruitsandvegetables") == "TRUE"):  # Проверяем если мясо включенно
            db.update(call.from_user.id, "FALSE", "fruitsandvegetables")
            # обновляем
            catergories(call)
        else:
            db.update(call.from_user.id, "TRUE", "fruitsandvegetables")
            # обновляем
            catergories(call)
    # -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-= КОНДИТЕРСКИЕ ИЗДЕЛИЯ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-
    if call.data == "confection":
        if (db.check(call.from_user.id, "confection") == "TRUE"):  # Проверяем если мясо включенно
            db.update(call.from_user.id, "FALSE", "confection")
            # обновляем
            catergories(call)
        else:
            db.update(call.from_user.id, "TRUE", "confection")
            # обновляем
            catergories(call)
    # -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-= ХЛЕБОБУЛОЧНЫЕ ИЗДЕЛИЯ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-
    if call.data == "bakery":
        if (db.check(call.from_user.id, "bakery") == "TRUE"):  # Проверяем если мясо включенно
            db.update(call.from_user.id, "FALSE", "bakery")
            # обновляем
            catergories(call)
        else:
            db.update(call.from_user.id, "TRUE", "bakery")
            # обновляем
            catergories(call)
    # -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-= ЯЙЦА -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-
    if call.data == "eggs":
        if (db.check(call.from_user.id, "eggs") == "TRUE"):  # Проверяем если мясо включенно
            db.update(call.from_user.id, "FALSE", "eggs")
            # обновляем
            catergories(call)
        else:
            db.update(call.from_user.id, "TRUE", "eggs")
            # обновляем
            catergories(call)
    # -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-= ПТИЦА -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-
    if call.data == "bird":
        if (db.check(call.from_user.id, "bird") == "TRUE"):  # Проверяем если мясо включенно
            db.update(call.from_user.id, "FALSE", "bird")
            # обновляем
            catergories(call)
        else:
            db.update(call.from_user.id, "TRUE", "bird")
            # обновляем
            catergories(call)
    # -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-= КРУПЫ И ТД -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-
    if call.data == "cereals":
        if (db.check(call.from_user.id, "cereals") == "TRUE"):  # Проверяем если мясо включенно
            db.update(call.from_user.id, "FALSE", "cereals")
            # обновляем
            catergories(call)
        else:
            db.update(call.from_user.id, "TRUE", "cereals")
            # обновляем
            catergories(call)
    # -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-= КОНСЕРВЫ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-
    if call.data == "canned":
        if (db.check(call.from_user.id, "canned") == "TRUE"):  # Проверяем если мясо включенно
            db.update(call.from_user.id, "FALSE", "canned")
            # обновляем
            catergories(call)
        else:
            db.update(call.from_user.id, "TRUE", "canned")
            # обновляем
            catergories(call)
    # -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-= ДРУГОЕ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-
    if call.data == "other":
        if (db.check(call.from_user.id, "other") == "TRUE"):  # Проверяем если мясо включенно
            db.update(call.from_user.id, "FALSE", "other")
            # обновляем
            catergories(call)
        else:
            db.update(call.from_user.id, "TRUE", "other")
            # обновляем
            catergories(call)
        # -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    if call.data == "category-finish":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        next = types.KeyboardButton(text="Настройки бота")
        keyboard.add(next)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вы успешно заполнили данные!😉 \nСкоро Вы начнете получать уведомления о новых "
                              "раздачах \n",
                         reply_markup=keyboard)

        while True:
            for i in range(len(vk_data.DOMAINS)):
                PARAMS = {
                    'domain': vk_data.DOMAINS[i].split('/')[-1],
                    'count': vk_data.COUNT,
                    'v': vk_data.VK_API_VERSION,
                    'access_token': vk_data.ACCESS_TOKEN
                }

                data = vk_data.get_new_posts(PARAMS)
                if data is not None:
                    for post in data:
                        users = db.ussr()
                        print(users)
                        o = 0
                        for i in range(len(users)):
                            print("Новый пост")
                            if len(post) > 0:
                                idd = list(users)
                                print("Работаю с пользователем: ")
                                print(idd[int(o)][0])

                                if (db.check(idd[int(o)][0], "meat") == "TRUE"):  #ЕСЛИ У ЧЕЛОВЕКА ВКЛЮЧЕННО МЯСО
                                    if "говядина" in post[1] or "корова" in post[1] or "як" in post[1] or "баранина" in post[1] or "свинина" in post[1] or "конина" in post[1] or "козлятина" in post[1] or "колбаса" in post[1] or " сало" in post[1] or "холодец" in post[1] or "фарш" in post[1] or " ветчина" in post[1] or "бекон" in post[1] or "котлеты" in post[1] or "замороженное мясо" in post[1] or "кролик" in post[1] or "полуфабрикат из говядины" in post[1] or "полуфабрикат из свинины" in post[1] or "сосиски" in post[1] or "сардельки" in post[1] or "зельцы" in post[1] or "мясные снеки" in post[1] or "стейк" in post[1]:
                                        bot.send_message(chat_id=idd[int(o)][0], text="#мясо \n\n" + post[1] + "\n\nСсылка: " + post[0])

                                if (db.check(idd[int(o)][0], "fish") == "TRUE"):  #ЕСЛИ У ЧЕЛОВЕКА ВКЛЮЧЕННО РЫБА
                                    if "рыба" in post[1] or "рыбёха" in post[1] or "карась" in post[1]: #И В ПОСТЕ СОДЕРЖИТСЯ УПОМНИНАНИЕ О РЫБЕ ПО КЛЮЧЕВЫМ СЛОВАМ
                                        bot.send_message(chat_id=idd[int(o)][0], text="#рыба \n\n" + post[1] + "\n\nСсылка: " + post[0])

                                if (db.check(idd[int(o)][0], "milk") == "TRUE"):  #ЕСЛИ У ЧЕЛОВЕКА ВКЛЮЧЕННО МОЛОЧНАЯ ПРОДУКЦИЯ
                                    if "молоко" in post[1] or "творог" in post[1] or "молочка" in post[1]: #И В ПОСТЕ СОДЕРЖИТСЯ УПОМНИНАНИЕ О МОЛОЧНЫМ ПРОДУКТАМ ПО КЛЮЧЕВЫМ СЛОВАМ
                                        bot.send_message(chat_id=idd[int(o)][0], text="#молочные_продукты \n\n" + post[1] + "\n\nСсылка: " + post[0])

                                if (db.check(idd[int(o)][0], "drinks") == "TRUE"):  #ЕСЛИ У ЧЕЛОВЕКА ВКЛЮЧЕННЫ НАПИТКИ
                                    if "напитки" in post[1] or "пить" in post[1] or "вода" in post[1]: #И В ПОСТЕ СОДЕРЖИТСЯ УПОМНИНАНИЕ О МОЛОЧНЫМ ПРОДУКТАМ ПО КЛЮЧЕВЫМ СЛОВАМ
                                        bot.send_message(chat_id=idd[int(o)][0], text="#напитки \n\n" + post[1] + "\n\nСсылка: " + post[0])

                                if (db.check(idd[int(o)][0], "fruitsandvegetables") == "TRUE"):  #ЕСЛИ У ЧЕЛОВЕКА ФРУКТЫ И ОВОЩИ
                                    if "овощи" in post[1] or "фрукты" in post[1] or "бананы" in post[1]: #И В ПОСТЕ СОДЕРЖИТСЯ УПОМНИНАНИЕ О ФРУКТАМ И ОВОЩАМ ПО КЛЮЧЕВЫМ СЛОВАМ
                                        bot.send_message(chat_id=idd[int(o)][0], text="#фрукты_и_овощи \n\n" + post[1] + "\n\nСсылка: " + post[0])

                                if (db.check(idd[int(o)][0], "confection") == "TRUE"):  #ЕСЛИ У ЧЕЛОВЕКА ВКЛЮЧЕННЫ КОНДИТЕРСКИЕ ИЗДЕЛИЯ
                                    if "кондитерские" in post[1] or "пирог" in post[1] or "печенье" in post[1] or "шоколадка" in post[1]: #И В ПОСТЕ СОДЕРЖИТСЯ УПОМНИНАНИЕ О КОНДИТЕРСКИХ ИЗДЕЛИЯХ ПО КЛЮЧЕВЫМ СЛОВАМ
                                        bot.send_message(chat_id=idd[int(o)][0], text="#кондитерские_изделия \n\n" + post[1] + "\n\nСсылка: " + post[0])

                                if (db.check(idd[int(o)][0], "bakery") == "TRUE"):  #ЕСЛИ У ЧЕЛОВЕКА ВКЛЮЧЕННЫ ХЛЕБОБУЛОЧНЫЕ ИЗДЕЛИЯ
                                    if "хлеб" in post[1] or "булки" in post[1] or "булочки" in post[1] or "шоколадка" in post[1]: #И В ПОСТЕ СОДЕРЖИТСЯ УПОМНИНАНИЕ О ХЛЕБОБУЛОЧНЫМ ИЗДЕЛИЯХ ПО КЛЮЧЕВЫМ СЛОВАМ
                                        bot.send_message(chat_id=idd[int(o)][0], text="#хлебобулочные_изделия \n\n" + post[1] + "\n\nСсылка: " + post[0])

                                if (db.check(idd[int(o)][0], "eggs") == "TRUE"):  #ЕСЛИ У ЧЕЛОВЕКА ВКЛЮЧЕННЫ ЯЙЦА
                                    if "яички" in post[1] or "яйца" in post[1] or "яйца" in post[1]: #И В ПОСТЕ СОДЕРЖИТСЯ УПОМНИНАНИЕ О ЯЙЦАХ ИЗДЕЛИЯХ ПО КЛЮЧЕВЫМ СЛОВАМ
                                        bot.send_message(chat_id=idd[int(o)][0], text="#яйца \n\n" + post[1] + "\n\nСсылка: " + post[0])

                                if (db.check(idd[int(o)][0], "bird") == "TRUE"):  #ЕСЛИ У ЧЕЛОВЕКА ВКЛЮЧЕННЫ ЯЙЦА
                                    if "птица" in post[1] or "курица" in post[1] or "чикенмакнагетс" in post[1]: #И В ПОСТЕ СОДЕРЖИТСЯ УПОМНИНАНИЕ О ЯЙЦАХ ИЗДЕЛИЯХ ПО КЛЮЧЕВЫМ СЛОВАМ
                                        bot.send_message(chat_id=idd[int(o)][0], text="#птица \n\n" + post[1] + "\n\nСсылка: " + post[0])

                                if (db.check(idd[int(o)][0], "cereals") == "TRUE"):  #ЕСЛИ У ЧЕЛОВЕКА КРУПЫ МАКАРОНЫ И ТД
                                    if "каша" in post[1] or "крупа" in post[1] or "гречка" in post[1] or "макароны" in post[1] or "лапшка" in post[1]: #И В ПОСТЕ СОДЕРЖИТСЯ УПОМНИНАНИЕ О КРУПЫ МАКАРОНЫ И ТД ПО КЛЮЧЕВЫМ СЛОВАМ
                                        bot.send_message(chat_id=idd[int(o)][0], text="#крупы #макаронные_изделия \n\n" + post[1] + "\n\nСсылка: " + post[0])

                                if (db.check(idd[int(o)][0], "canned") == "TRUE"):  #ЕСЛИ У ЧЕЛОВЕКА КОНСЕРВЫ
                                    if "шпроты" in post[1] or "консервы" in post[1] or "шпротная диета" in post[1]: #И В ПОСТЕ СОДЕРЖИТСЯ УПОМНИНАНИЕ О КОНСЕРВАХ ПО КЛЮЧЕВЫМ СЛОВАМ
                                        bot.send_message(chat_id=idd[int(o)][0], text="#консервы \n\n" + post[1] + "\n\nСсылка: " + post[0])

                                if (db.check(idd[int(o)][0], "other") == "TRUE"):  #ЕСЛИ У ЧЕЛОВЕКА КОНСЕРВЫ
                                    if "кетчуп" in post[1] or "приправа" in post[1]: #И В ПОСТЕ СОДЕРЖИТСЯ УПОМНИНАНИЕ О ДРУГОМ
                                        bot.send_message(chat_id=idd[int(o)][0], text="#другое \n\n" + post[1] + "\n\nСсылка: " + post[0])
                                o = o + 1
            time.sleep(60)

    # ОБРАБОТКА ТОЛЬКО НАСТРОЕК БОТА
    if call.data == "edit-city":  # редачим город
        keyboardmain = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(text="Новосибирск", callback_data="edit-novosibirsk")
        #btn2 = types.InlineKeyboardButton(text="Москва", callback_data="edit-moscow")
        keyboardmain.add(btn1)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Выберите город на который нужно изменить:",
                              reply_markup=keyboardmain)

    if call.data == "edit-novosibirsk":  # выбрали нск:
        keyboardmain = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Назад", callback_data="category-finish")
        keyboardmain.add(btn1)
        db.update_city(call.from_user.id, "nsk")
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Город изменён на Новосибирск",
                              reply_markup=keyboardmain)

    if call.data == "edit-moscow":  # выбрали нск:
        keyboardmain = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Назад", callback_data="category-finish")
        keyboardmain.add(btn1)
        db.update_city(call.from_user.id, "msk")
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Город изменён на Москва",
                              reply_markup=keyboardmain)



@bot.message_handler(content_types=['text'])  # Если пришло текстове сообщение
def mess(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "настройки бота":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(text="Изменить категории", callback_data="select-category")
        btn2 = types.InlineKeyboardButton(text="Изменить город", callback_data="edit-city")
        btn3 = types.InlineKeyboardButton(text="Назад", callback_data="category-finish")
        markup.add(btn1, btn2, btn3)
        bot.send_message(chat_id=message.chat.id,
                         text="Настройки:",
                         reply_markup=markup)


if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            # повторяем через 15 секунд в случае недоступности сервера Telegram
            time.sleep(15)
