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
                songs = json.load(sfile)
        except Exception as e:
            print("Got exception while fetching songs from songs.json")
            traceback.print_exc()
        return songs

    def getSongsList(self):
        """
        Method for returning a song on demand
        :return:
        """
        songsList = self.loadSongs()
        return songsList

    def getSongsByArtist(self, artistname):
        """
        Method for returning list of songs of a
        particular artist
        :param: artistname
        :return: songs list of particular artist
        """
        artistSongs = []
        songsList = self.loadSongs()
        artistSongs = [song for song in songsList if song.get("artist") == artistname]
        return artistSongs
