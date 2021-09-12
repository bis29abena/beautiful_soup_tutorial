# Scrapping the Ycombinator website
# Finding the highest search site in news.ycombinator.com

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
y_cm_web = response.text

soup = BeautifulSoup(y_cm_web, "html.parser")
article = soup.findAll(name="a", class_="storylink")
article_points = soup.findAll(name="span", class_="score")

articles_text = [tags.getText() for tags in article]
articles_link = [tags.get("href") for tags in article]
scores = [int(tags.getText().split()[0]) for tags in article_points]
maximum_score = max(scores)
index_of_max = scores.index(maximum_score)

print(articles_text[index_of_max])
print(articles_link[index_of_max])
print(maximum_score)








