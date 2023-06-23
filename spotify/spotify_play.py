#!/usr/bin/python3
import json
import spotipy
import webbrowser
from decouple import config


username = config('SPOTIFY_USER')
clientID = config('SPOTIFY_CLIENT_ID')
clientSecret = config('SPOTIFY_CLIENT_SECRET')
redirect_uri = 'http://localhost/'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()

print(user_name)
