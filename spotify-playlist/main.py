from bs4 import BeautifulSoup
import requests

URL = "https://www.billboard.com/charts/hot-100/"
date = input("Which date do you want to travel to? (YYYY-MM-DD): ")

response = requests.get(f"{URL}" + date)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

songs = soup.select("li ul li h3")
songs_list = [song.getText().strip() for song in songs]
print(songs_list)

