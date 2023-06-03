import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
data = []

for i in range(1, 6):
    print(i)
    # URL страницы
    url = f"https://www.kinopoisk.ru/lists/movies/genre--anime/?sort=rating&page={i}"

    # Отправляем GET-запрос на страницу
    response = requests.get(url)
    sleep(5)
    # Парсим HTML-страницу с помощью BeautifulSoup
    soup = BeautifulSoup(response.content, 'lxml')

    films = soup.findAll('div', class_='styles_root__ti07r')

    for film in films:
        link = "https://www.kinopoisk.ru" + film.find('a', class_='base-movie-main-info_link__YwtP1').get('href')
        russian_name = film.find('a', class_='base-movie-main-info_link__YwtP1')\
            .find('div', class_='base-movie-main-info_mainInfo__ZL_u3').text
        original_name = film.find('a', class_='base-movie-main-info_link__YwtP1')\
            .find('div', class_='desktop-list-main-info_secondaryTitleSlot__mc0mI')\
            .find('span', class_='desktop-list-main-info_secondaryTitle__ighTt').text
        country = film.find('a', class_='base-movie-main-info_link__YwtP1')\
            .find('div', class_='desktop-list-main-info_additionalInfo__Hqzof')\
            .find('span', class_='desktop-list-main-info_truncatedText__IMQRP').text
        rate = film.find('div', class_='styles_kinopoiskValueBlock__qhRaI').text
        data.append([link, russian_name, original_name, country, rate])

header = ['link', 'russian name', 'original name', 'country', 'rate']
df = pd.DataFrame(data, columns=header)
df.to_csv('C:\\Users\\danii\\вход в гильдию\\kinopoisk_data.csv', sep=';', encoding='utf8')
print(len(data))