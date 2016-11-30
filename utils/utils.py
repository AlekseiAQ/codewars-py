import requests
from envs import *

language = 'python'
slug = 'head-tail-init-and-last'

headers = {
    'Authorization': API_KEY
}

data = {
  'strategy': 'random'
}

url = 'https://www.codewars.com/api/v1/users/{}'.format(USER_NAME)
kata_solution_url = 'https://www.codewars.com/api/v1/code-challenges/{}/{}/train'.format(
	slug, language)
# print(kata_solution_url)

# example
# r = requests.get(url, headers=headers)
# r = requests.post(kata_solution_url, headers=headers)

r = requests.get(url, headers=headers)




# r = requests.post('https://www.codewars.com/api/v1/code-challenges/anything-to-integer/javascript/train', headers=headers)

# kata = requests.get('https://www.codewars.com/api/v1/code-challenges/valid-braces')

print(r.status_code)

# print(r.json)
# print(r.text)

# print(r.json().keys())
# print(r.json()['username'])


# requests.post('https://www.codewars.com/api/v1/code-challenges/javascript/train', headers=headers, data=data)

