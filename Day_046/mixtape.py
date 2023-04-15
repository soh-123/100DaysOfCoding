from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
CACHE_PATH = {"access_token": "BQBBBe7TYp7uo1igD-VCZb9TCbecSXe5MQOwYvovrho4xCuH1ZVfATgfWWkxIYxbOxvLR3Lzt2LmyLsEYyILvqVOryRujSj1d-KO1RtULCqUQZ_3JZrEKXfVjEJa_w872MTNo3qemAnZ_Wok_fQ-ZAsn8nKV1r2rNpOzL_QxGBzLKnp8RmlZAvPE7iRUpRr_X-_lgtQ1tX8SEZJgX7zryrVpBKsJluAqccg7oSI", "token_type": "Bearer", "expires_in": 3600, "refresh_token": "AQAXJ9GQHAkySVzeohALfpN3mC-LswMD0JhBrbsUobkl3A1MjVxNtIW3NbVYnF6xoH-DhfCtUrhph4TOWAMRgmc4WJd8b9tMUG77iO4ZYyOBUxICz1Ez_RUJ07gOcWON4Ds", "scope": "playlist-modify-private", "expires_at": 1681108137}


#--------------------------------------100 BILLBOARD WEB SCRAPPING--------------------------------------------#

date = input("Which year would you like to travel? Type the date in YYY-MM-DDformat: ")
response = requests.get("https://www.billboard.com/charts/hot-100/"+date)

soup = BeautifulSoup(response.text, "html.parser")
song_title = soup.select(selector="li h3", class_="c-title")

song_names = [song.getText().strip() for song in song_title]

#--------------------------------------SPOTIFY AUTHENTICATION--------------------------------------------#

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path=CACHE_PATH))

user_id = sp.current_user()["id"]

#--------------------------------------SEARCH SPOTIFY SONG BY TITLE--------------------------------------------#

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#--------------------------------------ADDING SONGS TO A NEW PLAYLIST-------------------------------------------#

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)