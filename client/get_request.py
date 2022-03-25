import json
import requests

# Exemplo de GET


def call_get_request(url):

    resposta_hoteis = requests.request('GET', url + '/hoteis')

    resposta_hoteis.status_code

    hoteis = resposta_hoteis.json()

    # print(hoteis['hoteis'][0])
    lista_hoteis = hoteis['hoteis']
    for hotel in lista_hoteis:
        print(hotel['nome'])

    ML_URL = 'https://api.mercadolibre.com/sites'

    lista_sites = requests.request('GET', ML_URL)

    print(lista_sites)


def call_get_request_hotel(url):

    resposta_hoteis = requests.request('GET', url + '/hoteis/delta')

    print("status:",resposta_hoteis.status_code)

    hoteis = resposta_hoteis.json()

    print('Hoteis: ', hoteis)
