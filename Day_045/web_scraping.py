from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

news = soup.find_all(class_="titleline")
news_titles = []
news_links = []
for tag in news:
    news_titles.append(tag.find(name="a").getText())
    news_links.append(tag.find(name="a").get("href"))

news_votes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

index_vote = news_votes.index(max(news_votes))


print(news_titles[index_vote])
print(news_links[index_vote])
print(news_votes[index_vote])

