import requests
import os
import sys
import random
import pprint as p
import time

assert os.getenv('VALIDATIONCODE'), "Env variable VALIDATIONCODE should be set"
assert os.getenv('EMAIL'), "Env variable EMAIL should be set"

time.sleep(random.randint(0,59))

headers = {
    'authority': 'reservation.affluences.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'fr',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://affluences.com',
    'referer': 'https://affluences.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

json_data = {
    'validationCode': os.getenv('VALIDATIONCODE'),
    'email': os.getenv('EMAIL'),
}

response = requests.post('https://reservation.affluences.com/api/validateReservation', headers=headers, json=json_data)

p.pprint(f'response = {response} | response.text = {response.text}')

sys.exit(0)
