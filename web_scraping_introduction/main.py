from bs4 import BeautifulSoup
import requests


def find_highest_points(points_list, titles_list, links_list):
    highest_points = max(points_list)
    index = points_list.index(highest_points) + 1
    print(f"Most upvoted:\n{titles_list[index]}\n{links_list[index]}\n{highest_points} points")
    
    
response = requests.get("https://news.ycombinator.com/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
articles_titles = []
articles_links = []

for info in articles:
    title = info.get_text().split("(")[0]
    articles_titles.append(title)
    link = info.find(name="a").get("href")
    articles_links.append(link)
    
article_points = [int(points.get_text().split()[0]) for points in soup.find_all(name="span", class_="score")]

find_highest_points(article_points, articles_titles, articles_links)





