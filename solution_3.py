import datetime


class Album:
    """
    A class used to represent an Album.
    """
    all_albums = []

    def __init__(self, name_album, year_album, name_singer):
        """
        Initialize the Album instance.

        Parameters:
        name_album (str): The name of the album.
        year_album (int): The release year of the album.
        name_singer (str): The name of the singer.
        """
        self.name_album = name_album
        self.year_album = year_album
        self.name_singer = name_singer
        self.songs = []
        Album.singers(self)
        Album.all_albums.append(self)

    def singers(self):
        """
        Associate songs with the album if they match the album and singer.
        """
        for i in Song.all_songs:
            if i.name_singer == self.name_singer and i.name_album == self.name_album:
                self.songs.append(i)

    def __str__(self):
        """
        Return a string representation of the album and its songs.
        """
        return (f'Песни в альбоме: \n'
                f'{"\n".join([str(i) for i in self.songs])}')

    def __repr__(self):
        """
        Return an unambiguous string representation of the album.
        """
        return self.__str__()


class Song:
    """
    A class used to represent a Song.
    """
    all_songs = []

    def __init__(self, name_song, lasting, name_singer, year_song, name_album):
        """
        Initialize the Song instance.

        Parameters:
        name_song (str): The name of the song.
        lasting (str): The duration of the song in 'MM:SS' format.
        name_singer (str): The name of the singer.
        year_song (int): The release year of the song.
        name_album (str): The name of the album the song belongs to.
        """
        self.name_song = name_song
        self.lasting = '00:' + lasting
        self.name_singer = name_singer
        self.year_song = year_song
        self.name_album = name_album
        Song.all_songs.append(self)

    def __str__(self):
        """
        Return a string representation of the song.
        """
        if self.name_album == '':
            return (f'Название трека: {self.name_song}, Продолжительность трека: {self.lasting}, '
                    f'Имя певца: {self.name_singer}, Год выхода: {self.year_song}')
        return (f'Название трека: {self.name_song}, Продолжительность трека: {self.lasting}, '
                f'Имя певца: {self.name_singer}, Год выхода: {self.year_song}, Название альбома: {self.name_album}')

    def __repr__(self):
        """
        Return an unambiguous string representation of the song.
        """
        return self.__str__()


class Music:
    """
    A class used to represent Music being played.
    """
    playing_song = []

    def __init__(self, song):
        """
        Initialize the Music instance.

        Parameters:
        song (Song): An instance of the Song class.
        """
        self.song = song
        self.strt = 0
        self.fnsh = 0
        time_song = song.lasting.split(':')
        self.last = datetime.timedelta(seconds=int(time_song[2])+int(time_song[1])*60+int(time_song[0])*60*24)
        Music.playing_song.append(self)

    def start(self):
        """
        Start playing the song and calculate the finish time.
        """
        self.strt = datetime.datetime.now()
        self.fnsh = self.strt + self.last
        return f'{self.__str__()},продолжительность трека: {self.last}'

    def finish(self):
        """
        Stop playing the song and remove it from the playing list.
        """
        Music.playing_song.remove(self)
        return f'{self.song.name_song} закончилась'

    def pause(self):
        """
        Pause the song and calculate the remaining time.
        """
        time_diff = self.fnsh - datetime.datetime.now()
        self.last = datetime.timedelta(seconds=time_diff.total_seconds())
        return f'{self.song.name_song} на паузе, до конца трека: {self.last}'

    def __str__(self):
        """
        Return a string representation of the music being played.
        """
        return f'{self.song.name_song} началась в {self.strt}, закончится в {self.fnsh}'

    def __repr__(self):
        """
        Return an unambiguous string representation of the music being played.
        """
        return self.__str__()
