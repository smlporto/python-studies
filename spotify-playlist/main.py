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
songs_list = [song.getText().strip() for song in songs]
print(songs_list)

