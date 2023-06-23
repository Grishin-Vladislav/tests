import requests
import time


class YaInterface:
    """
    Interface to provide base Yandex url,
     user token and auth request headers
    """
    url = 'https://cloud-api.yandex.net/v1/disk'

    def __init__(self, token: str) -> None:
        self.token = token
        self.headers = {
            'Accept': 'application/json',
            'Authorization': f'OAuth {token}'
        }


class YaDirectory(YaInterface):
    """
    Directory manager for cloud storage
    """

    def __init__(self, token: str) -> None:
        super().__init__(token)
        self.url = f'{self.url}/resources'

    def is_path_exists(self, path: str) -> bool:
        """
        Checks if directories or files exists
        :param path: directory path, ex:'docs/photos/meme.jpg'
        :return: True if all directories exists, else: False.
        """
        params = {'path': f'disk:/{path}'}
        response = requests.get(self.url, headers=self.headers, params=params)
        time.sleep(0.2)
        if response.status_code == 200:
            return True
        return False

    def create_folder(self, path: str) -> requests.Response:
        """
        Creates folder by given path, last destination will be desired folder
        :param path: path to desired folder ex:'docs/photos/memes'
        """
        params = {'path': f'disk:/{path}'}
        res = requests.put(self.url, headers=self.headers, params=params)
        time.sleep(0.2)
        return res
