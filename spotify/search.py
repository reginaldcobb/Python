# shows artist info for a URN or URL

import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import requests

import json

import sys
from pprint import pprint

cid = '8b00db826a894dbd8f444ee62ee02a2b'
secret = '289920cd4a1f4f49a7216cb14abf9035'

if len(sys.argv) > 1:
    urn = sys.argv[1]
else:
    urn = 'spotify:artist:3t58jfUhoMLYVO14XaUFLA'

    #https://open.spotify.com/artist/3t58jfUhoMLYVO14XaUFLA?si=F3gf-00xQj6EdTWZ86PQdA
    # https://open.spotify.com/artist/7aRi9OzdA2ciputfuguaPK?si=ZLFMWfNrSqyL2kTUfB-CpA

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=cid, client_secret=secret))

# search_str  = input("Please enter Artist:\n")
 
# print(f'You entered {search_str}')

# search_str = 'Radiohead'

# result = sp.search(search_str)
result = sp.search("name:Pat%20Methany",  type="artist")


# results = json.load(result)
# results = json.load(sp.search(search_str))
# print(result)

pprint(result)

# Serializing json 
json_object = json.dumps(result, indent = 4)
  
# Writing to sample.json
with open("search.json", "w") as outfile:
    outfile.write(json_object)


# https://open.spotify.com/artist/3t58jfUhoMLYVO14XaUFLA?si=RMzTFyNqQkugDgdoCVwcoQ