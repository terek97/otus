from .media_file import MediaFile

class AudioFile(MediaFile):
    def __init__(self, path, name, artist='unknown', album='unknown'):
        super().__init__(path, name)
        self._artist = artist
        self._album = album

    # getters
    @property
    def artist(self):
        return self._artist

    @property
    def album(self):
        return self._album

    # logic methods
    def from_mp3_to_wav(self):
        """
        Method to convert file format
        """
        print(f"file {self.name} was converted from mp3 to WAV")