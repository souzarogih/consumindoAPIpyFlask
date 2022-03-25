import json
import requests

# Exemplo de POST


def call_post_request_user(url):
    endpoint_cadastro = url + '/cadastro'

    print(endpoint_cadastro)

    body_cadastro = {
        'login': 'danilo',
        'senha': 'abc123'
    }

    headers_cadastro = {
        'Content-Type': 'application/json'
    }

    resposta_cadastro = requests.request('POST', endpoint_cadastro, json=body_cadastro, headers=headers_cadastro)

    print(resposta_cadastro)
    print(resposta_cadastro.json())


def call_post_request_login(url):
    endpoint_cadastro = url + '/login'

    print(endpoint_cadastro)

    body_cadastro = {
        'login': 'danilo',
        'senha': 'abc123'
    }

    headers_cadastro = {
        'Content-Type': 'application/json'
    }

    resposta_cadastro = requests.request('POST', endpoint_cadastro, json=body_cadastro, headers=headers_cadastro)

    print(resposta_cadastro)
    print(resposta_cadastro.json())
    print(resposta_cadastro.json()['access_token'])
    API_ACCESS_TOKEN = resposta_cadastro.json()['access_token']
    # Este variavel está sendo utilizada por outros métodos


def call_post_request_cadastro(url):
        endpoint_cadastro = url + '/cadastro'

        print(endpoint_cadastro)

        body_cadastro = {
            'login': 'rogih',
            'senha': 'abc123'
        }

        headers_cadastro = {
            'Content-Type': 'application/json'
        }

        resposta_cadastro = requests.request('POST', endpoint_cadastro, json=body_cadastro, headers=headers_cadastro)

        print(resposta_cadastro)
        print(resposta_cadastro.json())


def call_post_request_hotel(url, API_ACCESS_TOKEN):

    endpoint_hotel_id = url + '/hoteis/rogihhotel'
    print(endpoint_hotel_id)

    body_hotel_id = {
        'nome': 'Rogih Hotel',
        'estrelas': 4.8,
        'diaria': 398.90,
        'cidade': 'João Pessoa',
        "site_id": 3
    }

    headers_hotel_id = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + API_ACCESS_TOKEN
    }

    resposta_hotel_id = requests.request('POST', endpoint_hotel_id, json=body_hotel_id, headers=headers_hotel_id)

    print(resposta_hotel_id)
    print(resposta_hotel_id.json())
