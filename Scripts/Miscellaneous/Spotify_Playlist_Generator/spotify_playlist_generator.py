import argparse
import os
import random

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-public"
spotipy_instance = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, cache_path=os.getcwd()))


def get_args():
    parser = argparse.ArgumentParser(description='Split a playlist into multiple playlists')
    parser.add_argument('-p', '--playlist_id', required=True,
                        help='Playlist ID')
    parser.add_argument('-l', '--limit', required=True, default=20,
                        help='Size of each small playlist')
    return parser.parse_args()


def get_track_ids_for_playlist(playlist):
    res = []
    for song in playlist:
        res.append(song['track']['id'])
    return res


def generate_playlists(playlist_size, playlist_songs, user_id):
    smaller_playlists = [playlist_songs[x:x + playlist_size] for x in range(0, len(playlist_songs), playlist_size)]
    for index, playlist in enumerate(smaller_playlists):
        track_ids = get_track_ids_for_playlist(playlist)
        created_playlist = spotipy_instance.user_playlist_create(user_id, "generated_playlist_" + str(index + 1))
        spotipy_instance.playlist_add_items(created_playlist['id'], track_ids)
        print("Generated Playlist", str(index + 1), " of size", (playlist_size))


def main():
    args = get_args()

    playlist_size = int(args.limit)
    playlist_id = args.playlist_id

    print("Received Playlist ID :: ", playlist_id)

    playlist: dict = spotipy_instance.playlist_items(playlist_id)

    playlist_songs: list = playlist['items']

    user_id = spotipy_instance.me()['id']

    while playlist['next']:
        playlist = spotipy_instance.next(playlist)
        playlist_songs.extend(playlist['items'])

    print("Total songs in the given playlist :: ", str(len(playlist_songs)))

    random.shuffle(playlist_songs)

    generate_playlists(playlist_size, playlist_songs, user_id)


if __name__ == '__main__':
    main()
