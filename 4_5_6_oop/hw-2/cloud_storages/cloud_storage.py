from abc import ABC

class CloudStorage(ABC):
    def __init__(self, service_name):
        self._service_name = service_name

    # getters
    @property
    def service_name(self):
        return self._service_name

    # logic methods
    def upload(self, file):
        """Upload file to cloud cloud_storages"""
        print(f"{file} uploaded")

    def download(self, file, path):
        """Download file from cloud cloud_storages"""
        print(f"{file} downloaded")

    def delete(self, file):
        """Delete file from cloud cloud_storages"""
        print(f"{file} deleted")
