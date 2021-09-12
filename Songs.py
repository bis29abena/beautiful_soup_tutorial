# A python program to scrap the first 100 songs from the us bill board depending on the year
# The Scrapped list of songs would be added to your spotify playlist account

# ------------------------------- INSTRUCTION ----------------------- #
# Create a spotify account and access the developer mode
# In the developer look for create an app button to create your own
# After creating your own app you can access your client id and client key from there
# Then copy and paste those keys to the CLIENT_ID and CLIENT_KEY

# When you run the code url will pop up on your browser
# Accept that it is you and copy the url on the address bar
# Paste the copied url on the next prompt that appears on your console or terminal
# Then the playlist will be added to your spotify account 
# -------------------------------------------------------------------- #

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Client ID and Secret Key from spotify
CLIENT_ID = "Your Id here"
CLIENT_KEY = "Your secret key here"

# Taking the input year from the user
year = input("what year you would like to travel to in YYY-MM-DD format. ")

# Creating a reaponse variable to get the html content of the site
# Appending the year to the http site
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{year}")
# Saving the rext version of the response into billborad_site
billboard_site = response.text

# Using beautiful soup to parser the billboard_site into an html
soup = BeautifulSoup(billboard_site, "html.parser")
song_tile_tag = soup.findAll(name="span", class_="chart-element__information__song text--truncate color--primary")
song_title = [song.getText() for song in song_tile_tag]

# Accessing the spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_KEY,
                                               redirect_uri="http://bismark.com/callback/",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               ))
# Getting the user id from the spotify account
user_id = sp.current_user()["id"]

song_uri = []
# Getting Only the year from the date
year_ = year.split("-")[0]

# Searching through spotify to find the tracks in their library
for song in song_title:
    result = sp.search(q=f"track:{song} year:{year_}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)

    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a play list for the songs
playlist_id = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)["id"]

# Adding the songs to the play list
sp.playlist_add_items(playlist_id=playlist_id, items=song_uri)
