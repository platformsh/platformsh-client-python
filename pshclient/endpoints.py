from .base import *

SUBSCRIPTIONS_URL = '/api/platform/subscriptions'
PROJECT_LOCATOR_URL = '/api/platform/projects'
PROJECTS_URL = '/api/projects'

def subscriptions(subscription_id, method='get', data=None):
    '''
    Generic subscriptions endpoint.
    Takes a subscription_id, and optional method and data.
    '''
    return accounts_request(
        SUBSCRIPTIONS_URL + '/' + subscription_id,
        method,
        data
    )

def locator(project_id, method='get', data=None):
    '''
    Generic subscriptions project endpoint.
    Takes a session token, and optional method and data.
    '''
    return accounts_request(
        PROJECT_LOCATOR_URL + '/' + project_id,
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
