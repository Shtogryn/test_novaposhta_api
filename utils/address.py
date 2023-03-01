from collections import namedtuple

import os

from utils.http_methods import HttpMethods

BaseEndPoint = namedtuple('BaseEndPoint', ['base_url', 'api_key'])
URL = 'https://api.novaposhta.ua/v2.0/json/'
API_KEY = os.getenv("API_KEY")


class Address:

    @classmethod
    def create_body_request(cls, key, model, method, properties):
        return {
            "apiKey": key,
            "modelName": model,
            "calledMethod": method,
            "methodProperties": properties,
            "system": "DevCentre"
        }

    @classmethod
    def search_settlements(cls, city_name, limit, page):
        properties = {
            "CityName": city_name,
            "Limit": limit,
            "Page": page,
        }
        request = Address.create_body_request(API_KEY, 'Address', 'searchSettlements', properties)
        response = HttpMethods.post(URL, request)
        return response

    @classmethod
    def search_settlement_streets(cls, street_name, settlement_ref, limit):
        properties = {
            "StreetName": street_name,
            "SettlementRef": settlement_ref,
            "Limit": limit
        }
        request = Address.create_body_request(API_KEY, 'Address', 'searchSettlements', properties)
        response = HttpMethods.post(URL, request)
        return response

    @classmethod
    def get_street(cls, city_ref, find_by_string, limit, page) -> dict:
        properties = {
            'CityRef': city_ref,
            'FindByString': find_by_string,
            'Page': page,
            'Limit': limit
        }
        request = Address.create_body_request(API_KEY, 'Address', 'getStreet', properties)
        response = HttpMethods.put(URL, request)
        return response

    @classmethod
    def get_cities(cls, ref, find_by_string, limit):
        properties = {
            'Ref': ref,
            'FindByString': find_by_string,
            'Limit': limit
        }
        request = Address.create_body_request(API_KEY, 'Address', 'getCities', properties)
        response = HttpMethods.put(URL, request)
        return response

    @classmethod
    def save_counterparty_address(cls, counterparty_ref, street_ref, building_number, flat, note="Комментарий"):
        properties = {
            'CounterpartyRef': counterparty_ref,
            'StreetRef': street_ref,
            'BuildingNumber': building_number,
            'Flat': flat,
            'Note': note
        }
        request = Address.create_body_request(API_KEY, 'Address', 'searchSettlements', properties)
        request['apiKey'] = API_KEY
        response = HttpMethods.post(URL, request)
        return response

    @classmethod
    def delete_counterparty_address(cls, counterparty_ref):
        properties = {
            "Ref": counterparty_ref
        }
        request = Address.create_body_request(API_KEY, 'Address', 'searchSettlements', properties)
        request['apiKey'] = API_KEY
        response = HttpMethods.post(URL, request)
        return response
