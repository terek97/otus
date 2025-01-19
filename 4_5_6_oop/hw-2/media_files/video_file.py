from .media_file import MediaFile

class VideoFile(MediaFile):
    def __init__(self, path, name, resolution):
        super().__init__(path, name)
        self._resolution = resolution

    # getters
    @property
    def resolution(self):
        return self._resolution

    # logic methods
    def extract_frames(self):
        """Extracting frames from a video"""
        print(f"frame extracted from video file {self.name}")

    def compress_video(self, new_resolution):
        """Compressing video to new resolution"""
        if new_resolution < self._resolution:
            print(f"video file {self.name} compessed to {new_resolution} resolution")
        else:
            print("wrong resolution")