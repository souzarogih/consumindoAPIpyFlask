import json
import requests


def call_put_request_hotel(url, API_ACCESS_TOKEN):

    endpoint_hotel_id = url + '/hoteis/higuinhohotel'
    print(endpoint_hotel_id)

    body_hotel_id = {
        'nome': 'Guigo Hotel',
        'estrelas': 8.8,
        'diaria': 800.90,
        'cidade': 'Emirates',
        'site_id': 4
    }

    headers_hotel_id = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + API_ACCESS_TOKEN
    }

    resposta_hotel_id = requests.request('PUT', endpoint_hotel_id, json=body_hotel_id, headers=headers_hotel_id)

    print(resposta_hotel_id)
    print(resposta_hotel_id.json())