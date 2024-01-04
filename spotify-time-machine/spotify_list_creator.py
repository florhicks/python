import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

client_ID = os.environ.get("client_ID")
client_secret = os.environ.get("client_secret")

class SpotifyListCreator:
    def __init__(self, date):
        spotify_auth = spotipy.SpotifyOAuth(client_id=client_ID,
                                            client_secret=client_secret,
                                            redirect_uri="http://example.com",
                                            scope="playlist-modify-private",
                                            cache_path="token.txt",
                                            show_dialog=True)
        self.spotify = spotipy.Spotify(oauth_manager=spotify_auth)
        self.id_user = self.spotify.current_user()["id"]
        self.date = date
        self.year = self.date.split("-")[0]
        self.playlist_ID = self.create_playlist()

    def create_playlist(self):
        response = self.spotify.user_playlist_create(user=self.id_user,
                                                     name=f"Top 100 Billboard: {self.date}",
                                                     public=False,
                                                     description=f"Embark on a musical journey back in time to the "
                                                                 f"date: {self.date}")
        print(f"The link of playlist is: {response["external_urls"]["spotify"]}")
        return response["id"]

    def search_song_uri(self, song):
        result = self.spotify.search(q=f"track:{song} year:{self.year}", type="track", limit=1, market="AR")
        # pprint.pprint(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            return uri
        except IndexError:
            print(f"'{song}', doesn't exist in spotify. Skipped. ")

    def add_songs(self, songs):
        self.spotify.playlist_add_items(playlist_id=self.playlist_ID,
                                        items=songs)