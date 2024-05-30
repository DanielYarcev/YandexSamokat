#Ярцев Даниил 16-когорта финальный проект. Инжинер по тестированию рлюс

import sender_stand_request

import date


def test_order():

    response = sender_stand_request.post_create_order()
    if response.status_code == 201:
        return response.json()["track"]
    else:
        print(f"Ошибка: {response.status_code}")


def test_order_receive():
    track = test_order()
    response = sender_stand_request.get_order_receive(track)
    assert response.status_code == 200


