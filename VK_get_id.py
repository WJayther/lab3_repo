from base_client import BaseClient
import requests


class GetIDFromUsername(BaseClient):
    # users.get
    BASE_URL = 'https://api.vk.com/method/users.get'
    http_method = 'GET'

    def __init__(self, username):
        self.username = username

    def get_params(self):
        return 'user_ids='+self.username

    def response_handler(self, response):
        return response.json()['response'][0]['uid']

    def _get_data(self, method, http_method):
        response = requests.get(self.BASE_URL+'?'+self.get_params())

        return self.response_handler(response)


if __name__ == '__main__':
    test = GetIDFromUsername('wilhelmjayther')
    print(test.execute())
