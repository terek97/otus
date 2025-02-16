from .cloud_storage import CloudStorage

class YandexCloudStorage(CloudStorage):
    def __init__(self, account):
        super().__init__("Яндекс.Диск")
        self._account = account

    # getters
    @property
    def account(self):
        return self._account

    # logic methods
    def connect(self, password):
        """Connect to account.
        Other methods """
        print(f"successfully connected to account {self.account}")