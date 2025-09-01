import json
from urllib.parse import urljoin

import requests


class AuthError(Exception):
    def __init__(self, message):
        self.message = message


class LakasirError(Exception):
    def __init__(self, message='Failed to load data.'):
        self.message = message


class LakasirClient:
    def __init__(self, base_url, api_key=None, email=None, password=None):
        self.base_url = base_url
        self.api_key = api_key
        self.session = None

        if email and password:
            self.authenticate(email, password)

    def _url(self, path):
        return urljoin(self.base_url, path.lstrip('/'))

    def _api_call(self, method, path, **kwargs):
        request = requests.Request(method, self._url(path), **kwargs)

        session = requests.Session()
        session.headers.update({
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        })
        self.session = session

        response = session.send(self.session.prepare_request(request))

        if not response.ok:
            raise LakasirError(f'{response.status_code}: {json.dumps(response.json(), indent=2)}')

        try:
            data = response.json()
        except json.decoder.JSONDecodeError as e:
            raise e

        return data

    def authenticate(self, email, password):
        """Returns an object of token"""
        response = self._api_call('POST', f'/api/auth/login', json={
            'email': email,
            'password': password,
        })

        if 'token' not in response['data']:
            raise AuthError(response['message'])
        else:
            self.api_key = response['data']['token']

        return response

    def me(self):
        """Returns an object of User information"""
        return self._api_call('GET', f'/api/auth/me')

    def about(self):
        """Returns an object of Merchant information"""
        return self._api_call('GET', f'/api/about')

    def transaction_sells(self, timezone='UTC'):
        """Returns a list of transaction sells"""
        return self._api_call('GET', f'/api/transaction/selling?timezone={timezone}')

    def transaction_sells_with_page(self, page=1, per_page=30, timezone='UTC'):
        """Returns a list of transaction sells with pages"""
        return self._api_call('GET', f'/api/transaction/selling?page={page}&per_page={per_page}&timezone={timezone}')

    def total_sales(self, filter_type, timezone='UTC'):
        """Returns an object of total sales"""
        return self._api_call('GET', f'/api/transaction/dashboard/total-sales?filter_type={filter_type}&timezone={timezone}')

    def total_gross_profit(self, filter_type, timezone='UTC'):
        """Returns an object of total gross profit"""
        return self._api_call('GET', f'/api/transaction/dashboard/total-gross-profit?filter_type={filter_type}&timezone={timezone}')

    def total_revenue(self, filter_type, timezone='UTC'):
        """Returns an object of total revenue"""
        return self._api_call('GET', f'/api/transaction/dashboard/total-revenue?filter_type={filter_type}&timezone={timezone}')
