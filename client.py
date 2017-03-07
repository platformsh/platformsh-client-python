import requests
import json

BASE_URL = 'https://accounts.platform.sh'
TOKEN_URL = '/oauth2/token'
SUBSCRIPTIONS_URL = '/api/platform/subscriptions'

def get_session_token(api_token):
    '''
    Takes an api token and returns a session token if successful.
    Otherwise raises an error.
    '''
    headers = {
        # cGxhdGZvcm0tY2xpOg== is "platform-cli" in base64
        "Authorization": "Basic cGxhdGZvcm0tY2xpOg==",
        "Content-Type":"application/json"
    }
    data = {
        "grant_type": "api_token",
        "api_token": api_token,
    }
    res = requests.post(
        BASE_URL + TOKEN_URL,
        headers=headers,
        data=json.dumps(data),
    )
    return res.json()

def subscriptions(token, method='get', data=None):
    '''
    Takes a session token, and optional method and data.
    '''
    headers = {
        "Authorization": "Bearer {}".format(token),
        "Content-Type":"application/json"
    }
    if data:
        res = requests.request(
            method,
            BASE_URL + SUBSCRIPTIONS_URL,
            headers=headers,
            data=data
        )
    else:
        res = requests.request(
            method,
            BASE_URL + SUBSCRIPTIONS_URL,
            headers=headers,
        )
    return res.json()

if __name__ == "__main__":
    import sys
    res = get_session_token(sys.argv[1])
    print(res.json())
    print(subscriptions(res.json()['access_token'], method='get'))
