from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get("https://www.imdb.com/search/title/?at=0&genres=animation&keywords=anime&num_votes=1000,&sort=user_rating&title_type=tv_series", headers={"Accept-Language": "en-US,en;q=0.5"})

top_anime = response.text
soup = BeautifulSoup(top_anime, "html.parser")
anime_title = soup.find_all(name="h3", class_="lister-item-header")

anime_name = []
year = []

for title in anime_title:
    anime_name.append(title.find(name="a").get_text())
    year.append(title.find(name="span", class_="lister-item-year").get_text())

anime_genre = soup.find_all(name="span", class_="genre")
genre = [g.get_text() for g in anime_genre]

anime_vote = soup.find_all(name="span", attrs={'name': 'nv'})
votes = [v.get_text() for v in anime_vote]

new_table = pd.DataFrame({
    'Name':anime_name,
    'Genre':genre,
    'Year':year,
    'Votes':votes
    })

new_table.to_csv("Day_092/top_anime_list.csv")
