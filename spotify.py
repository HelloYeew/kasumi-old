import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

def spotify_first_search(keyword):
    results = sp.search(q=keyword, limit=1)
    result_dict = {}
    result_dict["name"] = results['tracks']['items'][0]['name']
    result_dict["artist_name"] = results['tracks']['items'][0]['album']['artists'][0]['name']
    result_dict["artist_url"] = results['tracks']['items'][0]['album']['artists'][0]['external_urls']['spotify']
    result_dict["album_name"] = results['tracks']['items'][0]['album']['name']
    result_dict["album_url"] = results['tracks']['items'][0]['album']['external_urls']['spotify']
    result_dict["image_url"] = results['tracks']['items'][0]['album']['images'][0]['url']
    result_dict["release_date"] = results['tracks']['items'][0]['album']['release_date']
    result_dict["popularity"] = results['tracks']['items'][0]['popularity']
    result_dict["available_country"] = results['tracks']['items'][0]['available_markets']
    result_dict["preview_url"] = results['tracks']['items'][0]['preview_url']
    result_dict["total_result"] = results['tracks']['total']
    return result_dict