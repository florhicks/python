from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movie_web_page = response.text

soup = BeautifulSoup(movie_web_page,"html.parser")

title_movies = soup.select(selector=".listicleItem_listicle-item__title__BfenH")
titles_text = [tag.getText() for tag in title_movies]
print(titles_text)

with open("100_movies.txt", mode='w') as file:
    for movie in titles_text:
        file.write(movie + '\n')