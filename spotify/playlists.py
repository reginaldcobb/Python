# Shows a user's playlists

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

import json
import uuid

cid = '8b00db826a894dbd8f444ee62ee02a2b'
secret = '289920cd4a1f4f49a7216cb14abf9035'
local_uri = 'http://localhost:8888/callback'

scope = 'playlist-read-private, playlist-modify-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid, client_secret=secret, redirect_uri=local_uri, scope=scope))

current_user_playlist_results = sp.current_user_playlists(limit=50)
for i, item in enumerate(current_user_playlist_results['items']):
    print("%d playlist:%s id:%s owner_id:%s" % (i, item['name'], item['id'], item['owner']['id']))

print (sp.me())
id = (sp.me()['id'])
print(id)

################
# Create Playlist
################

print ("Random id using uuid1() is : ",end="")
playlist_name = str(uuid.uuid1())
print (playlist_name)

# sp.user_playlist_create(id, 'Created with Python', public=False, collaborative=False, description='Created with Code')
sp.user_playlist_create(id, playlist_name, public=False, collaborative=False, description='Created with Code')

user_playlist_create_results = sp.user_playlists(id)
playlist_id = user_playlist_create_results['items'][0]['id']


# Serializing json 
json_object = json.dumps(user_playlist_create_results, indent = 4)
  
# Writing to sample.json
with open("current-playlist.json", "w") as outfile:
    outfile.write(json_object)


################
# BEGIN - Get Top Tracks
################

value = input("Please enter Artist Name:\n") 
print(f'You entered {value}')

# Find Artist URN
search_results = sp.search(value, limit=1)

# name = search_results['tracks']['items'][0]['album']['artists'][0]['name']
# id = search_results['tracks']['items'][0]['album']['artists'][0]['id']
uri = search_results['tracks']['items'][0]['album']['artists'][0]['uri']
# image_url = search_results['tracks']['items'][0]['album']['images'][0]['url']

# print ( name)
# print ( id)
print ( uri)
# print ( image_url)

artist_top_tracks_results = sp.artist_top_tracks(uri)

track_list = []

# for track in artist_top_tracks_results['tracks'][:10]:
for track in artist_top_tracks_results['tracks']:
    # print('link to track id: ' + track['id'])
    track_list.append(track['id'])

# PRint Json to file
# Serializing json 
# json_object = json.dumps(results, indent = 4)
  
# Writing to sample.json
# with open("tracks.json", "w") as outfile:
#     outfile.write(json_object)


################
# END - Get Top Tracks
################

################
# Add Top Track to Playlist
################

sp.user_playlist_add_tracks(user=id, playlist_id=playlist_id, tracks=track_list)


################
# Delete Playlist
################

# https://open.spotify.com/playlist/43ZErWr8dVU5wfJLYpderi?si=6de68429c06c46a6

# playlist_id = user_playlist_create_results['items'][0]['id']
value = input(f"Do you want to delete Playlist {playlist_id}: Yes/No\n") 
print(f'You entered {value} ')

if (value == "Yes"):
    sp.user_playlist_unfollow(id, playlist_id )
    print(f'You entered {value}, Playlist {playlist_id} will  be deleted')

