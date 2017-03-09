from .base import *

SUBSCRIPTIONS_URL = '/api/platform/subscriptions'
PROJECTS_URL = '/api/projects'

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

def settings(project, method='get', data=None):
    '''
    Generic settings endpoint. Takes a session token, project_id,
    environment name, and optional method and data.
    '''
    return platform_request(
        '{0}/{1}/{2}'.format(PROJECTS_URL, project, 'settings'),
        method,
        data
    )

def environments(project, environment='', method='get', data=None):
    '''
    Generic environments endpoint. Takes a project_id,
    environment name, and optional method and data.
    '''
    path = '/{project}/environments/{environment}'.format(
        project=project,
        environment=environment
    )
    res = platform_request(
        PROJECTS_URL + path,
        method,
        data,
    )
    return res

def projects(project='', method='get', data=None):
    '''
    Generic projects endpoint. Takes a, project_id,
    environment name, and optional method and data.
    '''
    return platform_request(
        PROJECTS_URL + '/' + project,
        method,
        data
    )
