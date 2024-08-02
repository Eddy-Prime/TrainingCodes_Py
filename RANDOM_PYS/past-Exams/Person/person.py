class Person:
    def __init__(self,name : str , age : int ,email : str):
        self.name = name
        self.age = age
        self.email = email
    
    @property
    def age(self):
        return self._age

    @property
    def email(self):
        return self._email
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0 :
            raise ValueError("age must be a positive integer!")
        age  = value

    @email.setter
    def email(self, sysmbol):
        if not isinstance(sysmbol, str) or "@" not in sysmbol or not sysmbol.strip():
            raise ValueError("string must contain "@"")
        self._email = sysmbol


class Movie:
    def __init__(self, title : str, director : str, release_year : int):
        self.title = title
        self.director = director
        self.release_year = release_year

    @property
    def director(self):
        return self._director

    @property
    def title(self):
        return self._title

    @property
    def release_year(self):
        return self._release_year

    @director.setter
    def director(self,value):
        if not isinstance(value, str) or not value.strip() : #non-empty strings
            raise ValueError("non-empty strings only!")
        self._director =  value

    @title.setter
    def title(self,value):
        if not isinstance(value, str) or not value.strip(): #non-empty strings
            raise ValueError("non-empty strings only!")
        self._title =  value

    @release_year.setter
    def release_year(self,value):
        if not isinstance(value, int) or value <= 0: #a positive integer.
            raise ValueError("Positive integer only!")
        self._release_year = value

    def get_details(self):
        return f"{self.title} by {self.director}, released in {self.release_year}"

#Song class
class Song:
    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist

    @property
    def title(self):
        return self._title

    @property
    def artist(self):
        return self._artist
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title must be a non-empty string!")
        self._title = value

    @artist.setter
    def artist(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Artist must be a non-empty string!")
        self._artist = value

#Playlist move song to a playlist
class Playlist:
    def __init__(self):
        self._songs = []

    def add_song(self, song):
        if not any(s.title.lower() == song.title.lower() and s.artist.lower() == song.artist.lower() for s in self._songs):
            self._songs.append(song)

    def remove_song(self, title, artist):
        title_lower = title.lower()
        artist_lower = artist.lower()
        self._songs = [s for s in self._songs if not (s.title.lower() == title_lower and s.artist.lower() == artist_lower)]

    def list_songs(self):
        return [f"{s.title} by {s.artist}" for s in self._songs]
