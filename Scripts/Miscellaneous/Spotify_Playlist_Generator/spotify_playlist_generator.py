import argparse
import os
import random

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-public"

# Create an instance of spotify library
spotipy_instance = spotipy.Spotify(
    auth_manager=SpotifyOAuth(scope=scope, cache_path=os.getcwd())
)


#
def get_args():
    """
    Method to read the command line arguments and parse them
    """

    parser = argparse.ArgumentParser(
        description="Split a playlist into multiple playlists"
    )
    # Required arguments for the program
    parser.add_argument(
        "-p", "--playlist_id", required=True, help="Playlist ID"
    )
    parser.add_argument(
        "-l",
        "--limit",
        required=True,
        default=20,
        help="Size of each small playlist",
    )
    return parser.parse_args()


# This method returns all the Spotify Song IDs from a given playlist
def get_track_ids_for_playlist(playlist):
    res = []
    for song in playlist:
        res.append(song["track"]["id"])  # Extract the ID of the track
    return res


def generate_playlists(playlist_size, playlist_songs, user_id):
    """
    This method generates smaller playlists from the input playlist
    """

    # Create the smaller playlists from the given large playlist
    smaller_playlists = [
        playlist_songs[x : x + playlist_size]
        for x in range(0, len(playlist_songs), playlist_size)
    ]
    for index, playlist in enumerate(smaller_playlists):
        # Once we have the smaller playlists we need to create them on the account
        # For that we need to extract IDS of the songs in the smaller playlists
        track_ids = get_track_ids_for_playlist(playlist)
        # Create the smaller playllist
        created_playlist = spotipy_instance.user_playlist_create(
            user_id, "generated_playlist_" + str(index + 1)
        )
        # Add songs to the playlist and publish them
        spotipy_instance.playlist_add_items(created_playlist["id"], track_ids)
        print(
            "Generated Playlist", str(index + 1), " of size", (playlist_size)
        )


def main():
    # Get the command line arguments
    args = get_args()

    # Extract playlist size from command line arguments
    playlist_size = int(args.limit)
    playlist_id = args.playlist_id

    print("Received Playlist ID :: ", playlist_id)

    # Get the playlist from spotify using the playlist ID
    playlist: dict = spotipy_instance.playlist_items(playlist_id)

    # Extract only the songs from the playlist, ignore extra metadata
    playlist_songs: list = playlist["items"]

    # Get the user_id of the user from the token
    user_id = spotipy_instance.me()["id"]

    while playlist["next"]:
        playlist = spotipy_instance.next(playlist)
        playlist_songs.extend(playlist["items"])

    print("Total songs in the given playlist :: ", str(len(playlist_songs)))

    # Shuffle the playlist
    random.shuffle(playlist_songs)

    # Now generate the smaller playlists
    generate_playlists(playlist_size, playlist_songs, user_id)


if __name__ == "__main__":
    main()
