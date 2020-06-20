# Сервисный ключ доступа Вконтакте
# Подробнее https://vk.com/dev/access_token
ACCESS_TOKEN = '533c22cf533c22cf533c22cfd8536ad1495533c533c22cf08b1a2cfba7856448603e1e2'

# Ссылка на метод API
# TODO: При расширении функционала можно создать отдельной настройкой выбор метода
# Подробнее https://vk.com/dev/methods
VK_API_LINK = 'https://api.vk.com/method/wall.get'

# Версия API
# Подробнее https://vk.com/dev/versions
VK_API_VERSION = '5.110'

# Количество записей, которое необходимо получить из каждой группы (ограничения Вконтакте не более 100)
# Подробнее https://vk.com/dev/wall.get
COUNT = '5'

# Количество дней, за которые были опубликованы записи
DAYS = 7

# Адреса сообществ Вконтакте
# TODO: Должны подгружаться из бызы и записываться в базу
DOMAINS = [
    'https://vk.com/etorussiadetka',
    'https://vk.com/free_eda',
    'https://vk.com/werpost'
]

# Слова для поиска
# TODO: Должны подгружаться из бызы и записываться в базу
PATTERNS = [
    'отдам',
    'подарю',
    'халявное'
]

# CATEGORIES = {
#     'Мясо': ['говядина', 'корова', 'як', 'баранина', 'свинина', 'конина', 'козлятина', 'колбаса', 'сало', 'холодец', 'фарш', 'ветчина', 'бекон', 'котлеты', 'замороженное мясо', 'кролик', 'полуфабрикат из говядины', 'полуфабрикат из свинины', 'сосиски', 'сардельки', 'зельцы', 'мясные снеки', 'стейк'],
#     'Рыба': ['анчоусы', 'вобла', 'горбуша', 'ерш', 'карась', 'карп', 'зубатка', 'кета', 'корюшка', 'мойва', 'окунь', 'семга', 'сом', 'треска', 'угорь', 'хек', 'форель', 'щука', 'икра', 'полуфабрикат белой рыбы', 'полуфабрикат красной рыбы', 'горячего копчения рыба', 'рыба красная слабой соли', 'рыба белой слабой соли', 'рыба сушеная', 'рыба вяленая', 'белая рыба', 'живая рыба', 'креветки', 'морепродукты', 'медуза', 'кальмар', 'осьминог', 'омар', 'лобстер', 'мидии', 'устрицы'],
#     'Молочные продукты': ['яйца куриные', 'яйца перепелиные', 'молоко', 'сливки', 'кефир', 'сметана', 'ацидофилин', 'йогурт', 'кумыс', 'простокваша', 'творог', 'сливочное масло', 'топленое масло', 'сыр', 'маргарин', 'спред', 'творожные десерты', 'сырок', 'тан', 'айран', 'мацони', 'пудинг', 'ряженка', 'творожная масса', 'сыворотка', 'ряженка'],
#     'Напитки': [вода, газированная вода, чай, кофе, сок, какао, горячий шоколад, цикорий, газированные напитки, кола, пепси, спрайт, миринда, энергетик, квас, алкоголь, пиво, вино, швепс, черноголовка, морс, 'нектары', 'спортивные напитки', 'вермут', 'безалкогольное', 'портвейн', 'кагор', 'шампанское', 'водка', 'виски', 'джин', 'абсент', 'текила', 'коньяк', 'ром', 'компот', 'кисель', 'липтон'],
#     'Фрукты, овощи, ягоды, грибы': [опята, лисичка, боровик, белый гриб, подберезовик, подосиновик, рыжик, маслята, шампиньон, грибы, сушеные грибы, баклажан, кабачок, зелень, замороженные овощи, редис, свекла, репа, 'картофель', 'морковь', 'капуста', 'огурец', 'помидор', 'квашеная капуста', 'томат', 'лук', 'салат', 'перец', 'чеснок', 'сельдерей корень', 'сельдерей', 'абрикос', 'ананас', 'слива', 'алыча', 'арбуз', 'дыня', 'банан', 'груша', 'яблоко', 'персик', 'нектарины', 'гранат', 'апельсин', 'мандарин', 'грейпфрут', 'лимон', 'кумкват', 'лайм', 'дуриан', 'авокадо', 'манго', 'кокос', 'киви', 'финики', 'физалис', 'арбуз', 'виноград', 'барбарис', 'брусника', 'бузина', 'годжи ягоды', 'голубика', 'вишня', 'клубника', 'ежевика', 'земляника', 'малина', 'ирга', 'калина', 'кизил', 'клюква', 'смородина', 'крыжовник', 'лимонник', 'морошка', 'облепиха', 'оливки', 'терн', 'фейхоа', 'черешня', 'черника', 'черемуха', 'шелковица', 'шиповник', 'виктория', 'помело', 'тушенные овощи', 'орехи', 'сухофрукты', 'миндаль'],
#     'Кондитерские изделия': [зефир, козинак, щербет, халва, чак-чак, мармелад, пастила, суфле, лукум, печенье, пряники, вафли, торты, пирожные, чизкейки, конфеты, сухофрукты в глазури, ирис, карамель, бисквит, торты, галеты, крекеры, пирожное, шоколадная паста, ореховая паста, шоколадки, снеки, печенье, чизкейк, леденцы, 'пастила', 'пирожное', 'кекс'],
#     'Хлебобулочные изделия': [хлеб, батон, булка, буханка, батон, бородинский, хлебцы, мука, выпечка, булочка, чиабатта, черный, белый, тарталетки, плетёнка, сухари, сухарики, плюшки, дрожжи, корж, рулет, сэндвич, багет, пирог, хлебцы, пирожок, лаваш.
#     'Готовые блюда': [бульон, запеканка, пицца, кимчи, пельмени, щи, салат, голубцы, детское питание, солянка, борщ, котлеты, макароны, картофельное пюре, плов, солянка, рассольник, блины, лазанья, мороженое, оладьи, манты, хинкали.
#     'Птица': [курица, индейка, полуфабрикаты из индейки, куриный фарш, куриный разруб, перепелка, филе, утенок, утка, куриные шейки, цыпленок.
#     'Крупы, макаронные изделия и бобовые':, [, вермишель, рожки, спагетти, лапша, ушки, ракушки, звездочки, колечки, паутинка, бантики, соломка спираль, макароны, гречка, гречневая крупа, рис, пшено, геркулес, нут, овес, манная крупа, овсяная крупа, рисовая крупа, чечевица, фасоль, горох, маш, ячмень, ячневая крупа, каша, манка],
#     'Консервы': [сайра, шпроты, консервированная кукуруза, консервированный горошек, килька, паштет, тушеная говядина, тушенка, семечки, оливки, маслины, сироп, мед.
#     'Другие категории': [ чайный гриб, джем, соус, смесь для выпечки, васаби, имбирь, майонез, суп, травяной сбор, варенье, закатка, банка, посыпка, приправа, пряности, арахисовая паста, кетчуп, соль, сахар, чипсы, аджика, горчица, хрен, уксус.
# }
