import json
import requests


def call_delete_request_hotel(url, API_ACCESS_TOKEN):

    endpoint_hotel_id = url + '/hoteis/higuinhohotel'
    print(endpoint_hotel_id)

    headers_hotel_id = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + API_ACCESS_TOKEN
    }

    resposta_delete_hotel = requests.request('DELETE', endpoint_hotel_id, headers=headers_hotel_id)

    print(resposta_delete_hotel)
    print(resposta_delete_hotel.json())


def call_delete_request_usuario(url, API_ACCESS_TOKEN):

    endpoint_hotel_id = url + '/usuarios/2'
    print(endpoint_hotel_id)

    headers_hotel_id = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + API_ACCESS_TOKEN
    }

    resposta_delete_usuario = requests.request('DELETE', endpoint_hotel_id, headers=headers_hotel_id)

    print(resposta_delete_usuario)
    print(resposta_delete_usuario.json())