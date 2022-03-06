# Top Tracks from Artist Name

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

import sys
from pprint import pprint
import json

cid = '8b00db826a894dbd8f444ee62ee02a2b'
secret = '289920cd4a1f4f49a7216cb14abf9035'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=cid, client_secret=secret))

value = input("Please enter Artist Name:\n") 
# print(f'You entered {value}')

# Find Artist URN
result = sp.search(value, limit=1)

name = result['tracks']['items'][0]['album']['artists'][0]['name']
id = result['tracks']['items'][0]['album']['artists'][0]['id']
uri = result['tracks']['items'][0]['album']['artists'][0]['uri']
image_url = result['tracks']['items'][0]['album']['images'][0]['url']

print (f'Name: {name}')
print (f'Artist ID: {id}')
print (f'Artist Link: {uri}')
print (f'Link to Image: {image_url}')
print ()

response = sp.artist_top_tracks(uri)

# for track in response['tracks'][:10]:
for track in response['tracks']:
    print('track    : ' + track['name'])
    # print('audio    : ' + track['preview_url'])
    # print('cover art: ' + track['album']['images'][0]['url'])
    # print('album: ' + track['album']['name'])

# PRint Json to file
# Serializing json 
json_object = json.dumps(response, indent = 4)
  
# Writing to sample.json
with open("top-tracks.json", "w") as outfile:
    outfile.write(json_object)