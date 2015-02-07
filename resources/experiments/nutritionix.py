import copy
import json
import os
import urllib

import requests


class SimpleKeyAuth(requests.auth.AuthBase):
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def __call__(self, request):
        request.headers['X-APP-ID'] = self.app_id
        request.headers['X-APP-KEY'] = self.app_key
        return request


class Client(requests.Session):
    API_URL = 'https://apibeta.nutritionix.com'
    USER_AGENT = 'recipi.me api client'

    def __init__(self, app_id, app_key):
        super(Client, self).__init__()
        self._auth = SimpleKeyAuth(app_id, app_key)

    def request(self, method, url, *args, **kwargs):
        headers = {
            'User-Agent': Client.USER_AGENT,
            'Method': method,
        }

        headers.update(kwargs.pop('headers', {}))

        kwargs.update({
            'auth': self._auth,
            'headers': headers,
        })

        full_url = urllib.parse.urljoin(Client.API_URL, url).rstrip('/')
        return super(Client, self).request(method, full_url, *args, **kwargs)
