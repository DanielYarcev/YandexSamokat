import configuration

import date

import create_user_test

import requests

def post_create_order():
    return requests.post(configuration.URL_SERVICE + configuration.RECEIVE_ORDER, headers=date.headers, json=date.body)
def get_order_receive(track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER + str(track))
