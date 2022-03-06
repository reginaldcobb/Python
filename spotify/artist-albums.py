# shows artist info for a URN or URL

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

import sys
from pprint import pprint

import argparse
import logging



logger = logging.getLogger('examples.artist_albums')
logging.basicConfig(level='INFO')


cid = '8b00db826a894dbd8f444ee62ee02a2b'
secret = '289920cd4a1f4f49a7216cb14abf9035'

if len(sys.argv) > 1:
    urn = sys.argv[1]
else:
    urn = 'spotify:artist:3t58jfUhoMLYVO14XaUFLA'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=cid, client_secret=secret))


def get_args():
    parser = argparse.ArgumentParser(description='Gets albums from artist')
    parser.add_argument('-a', '--artist', required=True,
                        help='Name of Artist')
    return parser.parse_args()


def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None


def show_artist_albums(artist):
    albums = []
    results = sp.artist_albums(artist['id'], album_type='album')
    albums.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    seen = set()  # to avoid dups
    albums.sort(key=lambda album: album['name'].lower())
    for album in albums:
        name = album['name']
        if name not in seen:
            logger.info('ALBUM: %s', name)
            seen.add(name)


def main():
    args = get_args()
    artist = get_artist(args.artist)
    if artist:
        show_artist_albums(artist)
    else:
        logger.error("Can't find artist: %s", artist)


if __name__ == '__main__':
    main()