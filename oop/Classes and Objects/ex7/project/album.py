from song import Song
class Album:
    def __init__(self, name, *args):
        self.name = name
        self.songs = list(args)
        self.published = False
    def add_song(self, song: Song):
        if self.published is True:
            return "Cannot add songs. Album is published."
        if song.single is True:
            return f"Cannot add {self.name}. It's a single"
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."
    def remove_song(self, song_name):
        if self.published is True:
            return "Cannot remove songs. Album is published."
        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."
    def publish(self):
        if self.published is True:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."
    def details(self):
        res = [f"Album {self.name}"]
        for song in self.songs:
            res.append(f"== {song.get_info()}")
        return "\n".join(res)
