import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=URL)
html_text = response.text
soup = BeautifulSoup(html_text)
movies = soup.select(selector='h3',class_="title" )
movies = movies[::-1]
for movie in movies:
    with open("favmovies.txt",'a') as file:
        file.write(str(movie.getText())+"\n")
    #print(movie.getText())
