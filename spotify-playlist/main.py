from bs4 import BeautifulSoup
import requests
from config import *
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
REDIRECT_URI = "https://example.com"

scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID, 
        client_secret=CLIENT_SECRET, 
        redirect_uri=REDIRECT_URI, 
        scope=scope,
        show_dialog=True,
        cache_path="token.txt"))

user_id = sp.current_user()["id"]

date = input("Which date do you want to travel to? (YYYY-MM-DD): ")

response = requests.get(f"{BILLBOARD_URL}" + date)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

songs = soup.select("li ul li h3")
songs_list = [song.getText().strip().replace("'","") for song in songs]

authors_list = []
authors = soup.find_all(name="span", class_="a-no-trucate")
for author in authors:
    clean_name = author.getText().lower().strip().split("featuring")[0].split(" / ")[0].split(" x ")[0].split(" & ")[0].split("with")[0]
    authors_list.append(clean_name)
#print(authors_list)    

songs_authors = []
for i in range(len(songs_list)):
    songs_authors.append((songs_list[i], authors_list[i]))
#print(songs_authors)

song_uris = []

for (song, author) in songs_authors:
    searched_song = sp.search(q=f"track: {song} artist:{author}", type="track")
    #print(searched_song)
    try:
        uri = searched_song["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} not found.")
        
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, collaborative=False, description=f"100 best songs at {date}")
playlist_id = playlist["id"]

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=song_uris, position=None)
        

