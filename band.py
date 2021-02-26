from project.album import Album
from project.song import Song

class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        filtered_album = [a for a in self.albums if a.name == album.name]
        if filtered_album:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        if album.published == True:
            return f"Album has been published. It cannot be removed."

        filtered_album = [a for a in self.albums if a.name == album.name]
        
        if filtered_album:
            album_to_remove = filtered_album[0]
            self.albums.remove(album_to_remove)
            return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f'Band {self.name}\n'
        for al in self.albums:
            result += f'{al.details()}\n'
        return result

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
