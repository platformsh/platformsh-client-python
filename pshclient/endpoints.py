from .base import *

SUBSCRIPTIONS_URL = '/api/platform/subscriptions'
ENVIRONMENTS_URL = '/api/projects'

def subscriptions(method='get', data=None):
    '''
    Generic subscriptions endpoint.
    Takes a session token, and optional method and data.
    '''
    return accounts_request(
        SUBSCRIPTIONS_URL,
        method,
        data
    )


def environments(project, environment='', method='get', data=None):
    '''
    Generic environments endpoint.
    Takes a session token, project_id, and optional method and data.
    '''
    path = '/{project}/environments/{environment}'.format(
        project=project,
        environment=environment
    )
    res = platform_request(
        ENVIRONMENTS_URL + path,
        method,
        data,
    )
    return res
