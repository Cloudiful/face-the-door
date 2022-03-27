# encoding:utf-8
import requests


def get_access_token(API_KEY, SECRET_KEY):
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + API_KEY + '&client_secret=' + SECRET_KEY
    response = requests.get(host)
    if response:
        return response.json()['access_token']
    else:
        return None
