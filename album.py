from project.song import Song

class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if self.published == True:
            return f"Cannot add songs. Album is published."

        filtered_song = [s for s in self.songs if s.name == song.name]

        if filtered_song:
            return f"Song is already in the album."

        else:
            if song.single == True:
                return f"Cannot add {song.name}. It's a single"

            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published == True:
            return "Cannot remove songs. Album is published."

        filtered_song = [s for s in self.songs if s.name == song.name]

        if filtered_song:
            song_to_remove = filtered_song[0]
            self.songs.remove(song_to_remove)
            return f'Removed song {song_name} from album {self.name}'
        return 'Song is not in the album.'

    def details(self):
        result = f'Album {self.name}\n'
        for s in self.songs:
            result += f'== {s.get_info()}\n'
        return result

    def publish(self):
        if self.published == True:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."




