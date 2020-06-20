"""В файле settings.py нужно задать:
    DOMAINS - группы для парсинга;
    COUNT - количество постов для анализа;
    DAYS - количество дней от текущей даты размещения объявления;
    PATTERNS - слова, которые ищем в постах.
    TODO: Вообще я думал группы и слова для парсинга из БД получать.
        В любом случае эти две переменные являются списками строк
"""

import vk_data

# Проходим по заданным ссылкам групп и формируем параметры для направления запросов к API
if __name__ == '__main__':

    for i in range(len(vk_data.DOMAINS)):
        PARAMS = {
            'domain': vk_data.DOMAINS[i].split('/')[-1],
            'count': vk_data.COUNT,
            'v': vk_data.VK_API_VERSION,
            'access_token': vk_data.ACCESS_TOKEN
        }

        # data = vk_data.search_food(vk_data.get_new_posts(PARAMS), vk_data.PATTERNS)
        data = vk_data.get_new_posts(PARAMS)
        if data is not None:
            for post in data:
                print(post[0])
                print(post[1])
                print()
                print()
