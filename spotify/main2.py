# shows artist info for a URN or URL

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

import sys
from pprint import pprint

cid = '8b00db826a894dbd8f444ee62ee02a2b'
secret = '289920cd4a1f4f49a7216cb14abf9035'

if len(sys.argv) > 1:
    urn = sys.argv[1]
else:
    urn = 'spotify:artist:3t58jfUhoMLYVO14XaUFLA'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=cid, client_secret=secret))

artist = sp.artist(urn)
pprint(artist)


# https://open.spotify.com/artist/3t58jfUhoMLYVO14XaUFLA?si=RMzTFyNqQkugDgdoCVwcoQ