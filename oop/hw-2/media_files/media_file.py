from datetime import datetime
from abc import ABC

class MediaFile(ABC):
    def __init__(self, path, name):
        self._path = path
        self._name = name
        self._creation_date = datetime.now()

    # getters
    @property
    def path(self):
        return self._path

    @property
    def name(self):
        return self._name

    @property
    def creation_date(self):
        return self._creation_date

    # logic methods
    def save(self):
        """
        Method to save file.
        The file will not be created on the specified path until this method is called.
        """
        print(f"file {self.name} saved")

    def delete(self):
        """
        Method to delete file
        """
        print(f"file {self.name} deleted")

    def update(self, *args):
        """
        Method to update file
        """
        print(f"file {self.name} updated")

    def rename_file(self, new_name):
        # some logic of file name changing
        old_name = self.name

        # and set _name property value
        self._name = new_name
        print(f"file {old_name} renamed to {self.name}")

    def move_file(self, new_path):
        # some logic of file path changing
        old_path = self.path

        # and set _path property value
        self._path = new_path
        print(f"file {old_path} renamed to {self.path}")