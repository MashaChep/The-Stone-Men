import telebot
from telebot import types
from base import SQLite
db = SQLite('database.db')
token = "1192793418:AAFt0guHDc8qZLCVVpUM6OIPmWjcVGGlU74"
bot = telebot.TeleBot(token)

#Вывод категорий
def catergories(ca):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    # -=-=-=-=-=- МЯЯЯЯЯСО --=-=-=-=-=-=
    if (db.category(ca.from_user.id, "meat") == "FALSE"):  # Проверяем если мясо включенно
        meattext = "Мясо"
    else:
        meattext = "Мясо ✅"
    btn1 = types.InlineKeyboardButton(text=meattext, callback_data="meat")
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # -=-=-=-=-=- РЫБА --=-=-=-=-=-=
    if (db.category(ca.from_user.id, "fish") == "FALSE"):  # Проверяем если рюба включенно
        fishtext = "Рыба"
    else:
        fishtext = "Рыба ✅"
    btn2 = types.InlineKeyboardButton(text=fishtext, callback_data="fish")
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # -=-=-=-=-=- МОЛОЧНЫЕ ПРОДУКТЫ --=-=-=-=-=-=
    if (db.category(ca.from_user.id, "milk") == "FALSE"):  # Проверяем если рюба включенно
        milktext = "Молоко"
    else:
        milktext = "Молоко ✅"
    btn3 = types.InlineKeyboardButton(text=milktext, callback_data="milk")
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # -=-=-=-=-=- НАПИТКИ --=-=-=-=-=-=
    if (db.category(ca.from_user.id, "drinks") == "FALSE"):  # Проверяем если рюба включенно
        drinkstext = "Напитки"
    else:
        drinkstext = "Напитки ✅"
    btn4 = types.InlineKeyboardButton(text=drinkstext, callback_data="drinks")
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # -=-=-=-=-=- Фрукты и овощи --=-=-=-=-=-=
    if (db.category(ca.from_user.id, "fruitsandvegetables") == "FALSE"):  # Проверяем если рюба включенно
        fruitsandvegetablestext = "Фрукты и овощи"
    else:
        fruitsandvegetablestext = "Фрукты и овощи ✅"
    btn5 = types.InlineKeyboardButton(text=fruitsandvegetablestext, callback_data="fruitsandvegetables")
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # -=-=-=-=-=- Кондитерские изделия --=-=-=-=-=-=
    if (db.category(ca.from_user.id, "confection") == "FALSE"):  # Проверяем если рюба включенно
        confectiontext = "Кондитерские изделия"
    else:
        confectiontext = "Кондитерские изделия ✅"
    btn6 = types.InlineKeyboardButton(text=confectiontext, callback_data="confection")
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # -=-=-=-=-=- Хлебобулочные изделия --=-=-=-=-=-=
    if (db.category(ca.from_user.id, "bakery") == "FALSE"):  # Проверяем если рюба включенно
        bakerytext = "Хлебобулочные изделия"
    else:
        bakerytext = "Хлебобулочные изделия ✅"
    btn7 = types.InlineKeyboardButton(text=bakerytext, callback_data="bakery")
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # -=-=-=-=-=- Яйца --=-=-=-=-=-=
    if (db.category(ca.from_user.id, "eggs") == "FALSE"):  # Проверяем если рюба включенно
        eggstext = "Яйца"
    else:
        eggstext = "Яйца ✅"
    btn8 = types.InlineKeyboardButton(text=eggstext, callback_data="eggs")
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # -=-=-=-=-=- Птица --=-=-=-=-=-=
    if (db.category(ca.from_user.id, "bird") == "FALSE"):  # Проверяем если рюба включенно
        birdtext = "Птица"
    else:
        birdtext = "Птица ✅"
    btn9 = types.InlineKeyboardButton(text=birdtext, callback_data="bird")
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # -=-=-=-=-=- Крупы, макаронные изделия и бобовые --=-=-=-=-=-=
    if (db.category(ca.from_user.id, "cereals") == "FALSE"):  # Проверяем если рюба включенно
        cerealstext = "Крупы, макаронные..."
    else:
        cerealstext = "Крупы, макаронные... ✅"
    btn10 = types.InlineKeyboardButton(text=cerealstext, callback_data="cereals")
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # -=-=-=-=-=- Консервы --=-=-=-=-=-=
    if (db.category(ca.from_user.id, "canned") == "FALSE"):  # Проверяем если рюба включенно
        cannedtext = "Консервы"
    else:
        cannedtext = "Консервы ✅"
    btn11 = types.InlineKeyboardButton(text=cannedtext, callback_data="canned")
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # -=-=-=-=-=- Другие категории --=-=-=-=-=-=
    if (db.category(ca.from_user.id, "other") == "FALSE"):  # Проверяем если рюба включенно
        othertext = "Остальное"
    else:
        othertext = "Остальное ✅"
    btn12 = types.InlineKeyboardButton(text=othertext, callback_data="other")
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    next = types.InlineKeyboardButton(text="Завершить выбор категорий", callback_data="category-finish")
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, next)
    bot.edit_message_text(chat_id=ca.message.chat.id,
                          message_id=ca.message.message_id,
                          text="Отлично! \nТемперь выберите категории из списка которые вас интересуют:",
                          parse_mode='html',
                          reply_markup=keyboard)


##########################################################################################################
