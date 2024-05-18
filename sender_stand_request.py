import configuration

import date

import create_user_test

import requests

def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)
response = post_create_order(date.body);

cod = response.json()

code = cod['track']

codes = str(code)

def get_order_receive():
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDER + codes)


