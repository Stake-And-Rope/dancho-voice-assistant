#!/usr/bin/python3


# Download your specific version for pycurl and compile it manually for your pc
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycurl

import pycurl
import requests


client_id = '1bc6f323006f4e808cc3f699309bdaec'
client_secret = 'c46f2c7b64bc43ebab1da3ee32e1c62b'

r = requests.get('https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb')
print(r)
