from pprint import pp, pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
cid = '8b00db826a894dbd8f444ee62ee02a2b'
secret = '289920cd4a1f4f49a7216cb14abf9035'

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# birdy_uri = 'spotify:artist:Pat%20Methany'
spotify = SpotifyClientCredentials(client_id=cid, client_secret=secret)

# results = spotify.artist_albums(birdy_uri, album_type='album')

results = spotify.artist(birdy_uri)
# albums = results['items']
pprint(results)

