from bs4 import BeautifulSoup
import requests
    
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

movies = soup.find_all(name="h3", class_="title")

with open("100-best-movies.txt", "w", encoding="utf-8") as file:
    for movie in movies[::-1]:
        title = movie.get_text()
        file.write(f"{title}\n")





