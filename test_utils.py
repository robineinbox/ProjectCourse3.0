import pytest

from utils import get_data, get_filtered_data, get_last_values, get_formated_data


@pytest.fixture
def test_data():
    return [
        {'date': '2019-08-26T10:50:58.294041',
         'description': 'Перевод организации',
         "id": 441945886,
         "operationAmount": {'amount': '31957.58',
                             "currency": {'code': 'RUB', 'name': 'руб.'}},
         'to': 'Счет 64686473678894779589'},
        {'date': '2019-07-03T18:35:29.512364',
         'description': 'Перевод организации',
         "from": 'Maestro 1596837868705199',
         "id": 41428829,
         "operationAmount": {'amount': '8221.37',
                             "currency": {'code': 'USD', 'name': 'USD'}},
         "state": 'EXECUTED',
         'to': 'Счет 64686473678894779589'},
        {'date': '2018-06-30T02:08:58.425572',
         'description': 'Перевод организации',
         "from": 'Счет 75106830613657916952',
         "id": 939719570,
         "operationAmount": {'amount': '9824.07',
                             "currency": {'code': 'USD', 'name': 'USD'}},
         "state": 'CANCELED',
         'to': 'Счет 64686473678894779589'},
        {'date': '2019-04-04T23:20:05.206878',
         'description': 'Перевод со счета на счет',
         "from": 'Счет 19708645243227258542',
         "id": 142264268,
         "operationAmount": {'amount': '79114.93',
                             "currency": {'code': 'USD', 'name': 'USD'}},
         "state": 'EXECUTED',
         'to': 'Счет 75651667383060284188'},
        {'date': '2019-03-23T01:09:46.296404',
         'description': 'Перевод организации',
         "from": 'Счет 44812258784861134719',
         "id": 873106923,
         "operationAmount": {'amount': '43318.34',
                             "currency": {'code': 'RUB', 'name': 'руб.'}},
         "state": 'EXECUTED',
         'to': 'Счет 74489636417521191160'}
    ]
def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    assert (len(get_filtered_data(test_data, filtered_empty_date=True))) == 3


def test_get_last_values(test_data):
    data = get_last_values(test_data, 2)
    assert ([x['date'] for x in data]) == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364']


def test_get_formated_data(test_data):
    data = get_formated_data(test_data[:1])
    assert (data) == ['\n        26.08.2019 Перевод организации\n         Счёт отправителя скрыт -> Счет **9589\n        31957.58 RUB\n        ']
    data = get_formated_data(test_data[1:2])
    assert (data) == [
        '\n        03.07.2019 Перевод организации\n        Maestro 1596 83** **** 5199 -> Счет **9589\n        8221.37 USD\n        '
    ]