#Ярцев Даниил 16-когорта финальный проект. Инжинер по тестированию рлюс

import sender_stand_request
import date



def test_order ():

    order_response = sender_stand_request.post_create_order(date.body);

    assert order_response.status_code == 201
def test_order_receive():
    order_receive = sender_stand_request.get_order_receive();

    assert order_receive.status_code == 200

