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

    def search_settlements(self, city_name, limit, page):
        properties = {
            "CityName": city_name,
            "Limit": limit,
            "Page": page,
        }
        request = Address.create_body_request(API_KEY, 'Address', 'searchSettlements', properties)
        response = HttpMethods.post(URL, request)
        return response

    def search_settlement_streets(self, street_name, settlement_ref, limit):
        properties = {
            "StreetName": street_name,
            "SettlementRef": settlement_ref,
            "Limit": limit
        }
        request = Address.create_body_request(API_KEY, 'Address', 'searchSettlements', properties)
        response = HttpMethods.post(URL, request)
        return response

    def get_street(self, city_ref, find_by_string, limit, page) -> dict:
        properties = {
            'CityRef': city_ref,
            'FindByString': find_by_string,
            'Page': page,
            'Limit': limit
        }
        request = Address.create_body_request(API_KEY, 'Address', 'getStreet', properties)
        response = HttpMethods.put(URL, request)
        return response

    def get_cities(self, ref, find_by_string, limit):
        properties = {
            'Ref': ref,
            'FindByString': find_by_string,
            'Limit': limit
        }
        request = Address.create_body_request(API_KEY, 'Address', 'getCities', properties)
        response = HttpMethods.put(URL, request)
        return response

    def save_counterparty_address(self, counterparty_ref, street_ref, building_number, flat, note="Комментарий"):
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

    def delete_counterparty_address(self, counterparty_ref):
        properties = {
            "Ref": counterparty_ref
        }
        request = Address.create_body_request(API_KEY, 'Address', 'searchSettlements', properties)
        request['apiKey'] = API_KEY
        response = HttpMethods.delete(URL, request)
        return response
