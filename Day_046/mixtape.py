from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"

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
    cache_path="Day_046/token.txt"))

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