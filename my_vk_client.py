from base_client import BaseClient
import requests
from datetime import datetime


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


class ParseFriends(BaseClient):
    # friends.get(fields=bdate)
    BASE_URL = 'https://api.vk.com/method/friends.get'
    http_method = 'GET'

    def __init__(self, uid):
        self.uid = uid

    def get_params(self):
        return 'user_id='+str(self.uid)+'&fields=bdate'

    def response_handler(self, response):
        friends = response.json()['response']
        hist = dict()
        for friend in friends:
            if 'bdate' in friend and friend['bdate'].count('.')==2:
                bdate = datetime.strptime(friend['bdate'], "%d.%m.%Y")
                curdate = datetime.now()
                difdate = curdate-bdate
                years = int(difdate.days // 365.25)
                if years not in hist:
                    hist[years] = 0
                hist[years] = hist[years]+1
        result_string = str()
        for age in sorted(hist):
            result_string = result_string + str(age) + ':'
            for i in range(hist[age]):
                result_string = result_string + '#'
            result_string = result_string + '\n'
        return result_string

    def _get_data(self, method, http_method):
        response = requests.get(self.BASE_URL+'?'+self.get_params())

        return self.response_handler(response)


if __name__ == '__main__':
    test = GetIDFromUsername('wilhelmjayther')
    uid = test.execute()
    test = ParseFriends(uid)
    print(test.execute())
