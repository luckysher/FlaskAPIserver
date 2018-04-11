import json
import traceback


class SongsUtils:
    """
    Class for Managing songs in json file. This class
    have the various methods for managing the songs like
    fetching songs list, fetching songs by artist etc..
    """

    def __init__(self):
        """
        constructor
        """
        self.songsFile = "settings/songs.json"

    def loadSongs(self):
        """
        Method for loading songs from songs.json file
        :return: songslist
        """
        songs = []
        try:
            with open(self.songsFile) as sfile:

        except Exception as e:

        return songs

    def getSongsList(self):
        """
        Method for returning a song on demand
        :return:
        """
        songsList = self.loadSongs()
        return songsList
