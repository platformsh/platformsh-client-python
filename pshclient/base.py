import requests
import os
import json
import sys

ACCOUNTS_URL = 'https://accounts.magento.cloud'
EU_PLATFORM_URL = 'https://eu.magento.cloud'
US_PLATFORM_URL = 'https://us.magento.cloud'
TOKEN_URL = '/oauth2/token'

class UserError(BaseException):
    pass

if not os.environ.get('MAGECLOUD_API_TOKEN'):
    # nothing to see here, just set your env variable
    sys.tracebacklimit = None
    raise UserError('Set the $MAGECLOUD_API_TOKEN environment variable.'
                    ' You can get your API Token under account settings at'
                    ' https://accounts.magento.cloud/user.'
                    )

def get_session_token(api_token=os.environ.get('MAGECLOUD_API_TOKEN')):
    '''
    Takes an api token and returns a session token if successful.
    Also caches the session token environment variable.
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
    import pdb; pdb.set_trace()
    res = requests.post(
        ACCOUNTS_URL + TOKEN_URL,
        headers=headers,
        data=json.dumps(data),
    )
    token = res.json()['access_token']
    os.environ['PLATFORMSH_SESSION_TOKEN'] = token
    return token

def accounts_request(endpoint, method='get', data=None):
    '''
    Request to the accounts endpoint.
    '''
    return base_request(ACCOUNTS_URL + endpoint, method, data)

def platform_request(endpoint, method='get', data=None, region=None):
    '''
    Request to the platformsh endpoints.
    '''
    if region is None:
        try:
            # try the US endpoint
            return base_request(
                US_PLATFORM_URL + endpoint,
                method,
                data
            )
        except:
            # try the EU endpoint
            return base_request(
                EU_PLATFORM_URL + endpoint,
                method,
                data
            )
    else:
        raise NotImplementedError

def base_request(url, method='get', data=None,
                 token=os.environ.get('PLATFORMSH_SESSION_TOKEN')):
    '''
    Attempts to revalidate the session token if it fails.
    '''
    if token is not None:
        try:
            return _base_request(url, token, method, data)
        except:
            token = get_session_token(os.environ.get('MAGECLOUD_API_TOKEN'))
            return _base_request(url, token, method, data)
    else:
        token = get_session_token(os.environ.get('MAGECLOUD_API_TOKEN'))
        return _base_request(url, token, method, data)


def _base_request(url, token, method, data):
    '''
    Generic authorized request.
    '''
    headers = {
        "Authorization": "Bearer {}".format(token),
        "Content-Type":"application/json"
    }
    if data:
        res = requests.request(
            method,
            url,
            headers=headers,
            data=data
        )
    else:
        res = requests.request(
            method,
            url,
            headers=headers,
        )
    return res.json()
