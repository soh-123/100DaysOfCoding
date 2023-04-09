from bs4 import BeautifulSoup
import requests
import re
import json

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_movies = response.text

movies = re.findall('titleText":"\d+\).*?"', empire_movies)

result = set()
for movie in movies:
    movie = movie.split(':"')[1]
    movie = movie.split(')')
    name = movie[1][:-1]
    rank = movie[0]
    result.add((int(rank), name))

movies = list(result)
movies.sort()
watched = []
need_to_watch = []
for rank, name in movies:
    print(str(rank) + ':' + name)
    answer = input("Did you watch that movie? y or n  ")
    if answer == "y":
        watched.append((rank,name))
    else:
        need_to_watch.append((rank, name))
    if rank == 100:
        print(need_to_watch)


with open("Day_045/movie.txt", mode="w") as file:
    for rank, name in need_to_watch:
        file.write(f"{rank}:{name}\n")
