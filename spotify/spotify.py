#!/usr/bin/python3
import json
import spotipy
import re
import webbrowser
from decouple import config
from spotipy.oauth2 import SpotifyOAuth


username = config('SPOTIFY_USER')
clientID = config('SPOTIFY_CLIENT_ID')
clientSecret = config('SPOTIFY_CLIENT_SECRET')
redirect_uri = 'http://localhost/'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()



scope = "user-read-playback-state,user-modify-playback-state"
#sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientID,
                                               client_secret=clientSecret,
                                               redirect_uri=redirect_uri,
                                               scope="user-read-playback-state,user-modify-playback-state"))

res = sp.devices()
#print(json.dumps(sp.current_playback()))


def play_track(search):
    result = sp.search(search, limit=1, type='track')
    pattern = r'https:\/\/open.spotify.com\/track\/\d\w{1,}'
    result = re.findall(pattern, str(result))
    #print(result)
    sp.start_playback(uris = result)



play_track('Neon Nox - Checkpoint')

