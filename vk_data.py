"""
Для запуска необходимо исполнить этот код

import vk_data

for i in range(len(vk_data.DOMAINS)):
    PARAMS = {
        'domain': vk_data.DOMAINS[i].split('/')[-1],
        'count': vk_data.COUNT,
        'v': vk_data.VK_API_VERSION,
        'access_token': vk_data.ACCESS_TOKEN
    }

    data = vk_data.search_food(vk_data.get_posts(PARAMS), vk_data.PATTERNS)
    if data is not None:
        for post in data:
            print(post[0])
            print(post[1])
            print()
            print()
"""

import datetime
import os
import re
import json
import requests
from settings import ACCESS_TOKEN, COUNT, DAYS, DOMAINS, PATTERNS, VK_API_LINK, VK_API_VERSION, CATEGORIES


def check_groups(domain):
    """Проверяет доступность группы по ссылке

        :raises

        :rtype: bool
        :return: True или False
    """
    get_connect = requests.get(f'https://vk.com/{domain}')
    if get_connect.status_code:
        return True
    else:
        return False


def get_new_posts(PARAMS):
    """Получает новые посты посты группы

            :raises

            :rtype: list
            :return: список кортежей со статьями [(ссылка, текст),]
        """
    if check_groups(PARAMS["domain"]):

        posts_dict = requests.get(VK_API_LINK, PARAMS).json()['response']['items']
        new_posts_list = []

        if not os.path.exists('last_post.txt'):
            data = {
                'groups': {
                    'owner_id': 'date',
                }
            }
            with open('last_post.txt', 'w') as f:
                json.dump(data, f)
        else:
            with open('last_post.txt', 'r') as f:
                data = json.load(f)

        for post in posts_dict:
            if post['text'] != '':
                publication_date = post['date']
                owner_id = str(post["owner_id"])
                if owner_id in data['groups'].keys():
                    if publication_date > data['groups'][owner_id]:
                        data['groups'][owner_id] = publication_date
                        new_posts_list.append((f'https://m.vk.com/wall{owner_id}_{post["id"]}', post['text']))
                else:
                    data['groups'][owner_id] = publication_date

                with open('last_post.txt', 'w') as f:
                    json.dump(data, f)

        return new_posts_list


def get_posts(PARAMS):
    """Получает посты группы

        :raises

        :rtype: list
        :return: список кортежей со статьями [(ссылка, текст),]
    """
    if check_groups(PARAMS["domain"]):
        posts_dict = requests.get(VK_API_LINK, PARAMS).json()['response']['items']
        posts_list = []
        for post in posts_dict:
            if post['text'] != '':
                publication_date = datetime.datetime.utcfromtimestamp(post['date'])
                now = datetime.datetime.now()
                days_ago = now - publication_date

                # Если дата размещения сегодня, то выдаем
                # if not days_ago.days:
                #     posts_list.append((f'https://m.vk.com/wall{post["owner_id"]}_{post["id"]}', post['text']))

                # Если опубликовано больше чем n дней назад (метод hours для часов)
                if days_ago.days <= DAYS:
                    posts_list.append((f'https://m.vk.com/wall{post["owner_id"]}_{post["id"]}', post['text']))

        return posts_list


def search_food(posts_list, search_patterns):
    """Ищет в объявлении из Вконтакте ключевые слова

        :param posts_list: список постов, полученный функцией get_posts()
        :type posts_list: list
        :param search_patterns: список шаблонов для поиска
        :type search_patterns: list

        :raises

        :rtype: list
        :return: список кортежей с найденными статьями [(ссылка, текст),] если нет статей то None
    """
    search_ads = []
    for post in posts_list:
        for pattern in search_patterns:
            # TODO: Второй вариант через регулярное выражение search_ads = re.search(r'not', title, re.I)
            if pattern.lower() in post[1].lower():
                search_ads.append(post)
                break
    if len(search_ads) > 0:
        return search_ads
