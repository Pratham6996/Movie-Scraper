import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
MOVIE = []
URLs = []
MOVIEs = []
i = 1
for x in range(1, 16):
    r = requests.get(f"https://www.themoviedb.org/movie?page={x}", headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    SOUP_CARD = soup.find_all('div', class_='card style_1')

    for MOVIE_PAGE in SOUP_CARD:
        for Ls in MOVIE_PAGE.find('div', class_='content').find_all('a', href=True):
            LINK = "https://www.themoviedb.org" + Ls['href']
            URLs.append(LINK)
for SEARCH_IN_PAGE in URLs:
    rp = requests.get(SEARCH_IN_PAGE, headers=headers)
    INFORMATION = BeautifulSoup(rp.content, 'lxml')
    MOVIE_NAME = INFORMATION.find('div', class_='title').a.text


    INFORMATION_DIV = INFORMATION.find('section', class_='header poster')
    try:
     DIRECTOR = INFORMATION.find('li', class_='profile').p.text.strip()
    except AttributeError:
      pass

    try:
      GENRE = INFORMATION.find('span', class_='genres').text.strip()
    except AttributeError:
        pass


    RELEASE_DATE = INFORMATION.find('span', class_='release').text.strip()

    try:
        DURATION = INFORMATION.find('span', class_='runtime').text.strip()
    except AttributeError:
        pass


    RATINGS = INFORMATION.find('div', class_='user_score_chart')['data-percent']
    MOVIEs = {
        'SR.No' : i,
        'MOVIE NAME': MOVIE_NAME,
        'Ratings': RATINGS,
        'GENRES': GENRE,
        'RELEASE DATE': RELEASE_DATE,
        'RUNTIME': DURATION,
        'DIRECTOR': DIRECTOR,
        'Url': SEARCH_IN_PAGE

    }
    i += 1
    MOVIE.append(MOVIEs)
df = pd.DataFrame(MOVIE)
print(df)
df.to_excel('MovieProject.xlsx')