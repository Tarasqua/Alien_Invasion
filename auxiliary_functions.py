import os


def create_playlist(dir_path: str):
    playlist = []
    for song in os.listdir(dir_path):
        playlist.append(f'{dir_path}/{song}')
    return playlist
