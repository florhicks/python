from song_search_engine import SongSearchEngine
from spotify_list_creator import SpotifyListCreator

date_songs = input("Which year do you want to travel? Type the date in this format YYYY-MM-DD"
                   ", if not, a default list will be returned ")
song_search = SongSearchEngine(date_songs)
song_list = song_search.song_list
spotify_list_creator = SpotifyListCreator(date_songs)

songs_uri = [spotify_list_creator.search_song_uri(song) for song in song_list]

spotify_list_creator.add_songs(songs_uri)