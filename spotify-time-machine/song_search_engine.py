from bs4 import BeautifulSoup
import requests

class SongSearchEngine:
    def __init__(self,date):
        self.song_date = date
        response = requests.get(f"https://www.billboard.com/charts/hot-100/{self.song_date}/")
        all_songs = response.text
        soup = BeautifulSoup(all_songs, features="html.parser")
        songs_name = soup.select("li ul li h3")
        self.song_list = [name.getText().strip() for name in songs_name]
