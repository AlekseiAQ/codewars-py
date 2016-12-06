import os.path
import sys
import requests
# import json
from .envs import API_KEY, USER_NAME

language = 'python'
# slug = 'triangular-treasure'

access_key = API_KEY


def get_kata_data(slug, access_key=API_KEY):
    url = 'https://www.codewars.com/api/v1/code-challenges/%s' % slug
    params = {'access_key': access_key}
    response = requests.get(url, params)
    if response.status_code == 200:
        data = response.json()
        kata_rank = abs(int(data['rank']['id']))
        return kata_rank
    else:
        raise Exception(response)


def create_files(slug):
    fname = '{}.py'.format(slug.replace('-', '_'))  
    if os.path.isfile(fname):
        print('Error... Files already exists...')
    else:
        with open(fname, 'w'), open('test_' + fname, 'w'):
            pass


# for key, value in data.items():
#     print(key)

# headers = {
#     'Authorization': API_KEY
# }

# data = {
#   'strategy': 'random'
# }