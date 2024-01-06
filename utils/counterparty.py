import os
from functools import reduce

from dotenv import load_dotenv
from utils.http_methods import HttpMethods

load_dotenv()
URL = 'https://api.novaposhta.ua/v2.0/json/'
API_KEY = os.getenv("API_KEY")


class Counterparty:
    @classmethod
    def create_body_request(cls, key, model, method, properties) -> dict:
        """

        :param key:
        :param model:
        :param method:
        :param properties:
        :return:
        """
        return {
            "apiKey": key,
            "modelName": model,
            "calledMethod": method,
            "methodProperties": properties,
            "system": "DevCentre"
        }

    @classmethod
    def save_counter_party(cls, first_name, middle_name, last_name, phone, email, counterparty_type, c_property):
        """

        :param first_name:
        :param middle_name:
        :param last_name:
        :param phone:
        :param email:
        :param counterparty_type:
        :param c_property:
        :return:
        """
        properties = {
            "FirstName": first_name,
            "MiddleName": middle_name,
            "LastName": last_name,
            "Phone": phone,
            "Email": email,
            "CounterpartyType": counterparty_type,
            "CounterpartyProperty": c_property
        }
        req = Counterparty.create_body_request(API_KEY, 'Counterparty', 'save', properties)
        response = HttpMethods.post(URL, req)
        return response

    @classmethod
    def delete_counter_party(cls, ref):
        """

        :param ref:
        :return:
        """
        properties = {
            'Ref': ref
        }
        req = Counterparty.create_body_request(API_KEY, 'Counterparty', 'delete', properties)
        response = HttpMethods.delete(URL, req)
        return response

    @classmethod
    def get_counter_parties(cls, counterparty_property, page):
        """

        :param counterparty_property:
        :param page:
        :return:
        """
        properties = {
            'CounterpartyProperty': counterparty_property,
            'Page': page
        }
        req = Counterparty.create_body_request(API_KEY, 'Counterparty', 'getCounterparties', properties)
        response = HttpMethods.post(URL, req)
        return response
