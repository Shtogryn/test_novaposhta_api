import requests


class HttpMethods:
    __headers = {'Content-Type': 'application/json'}

    @classmethod
    def get(cls, url):
        response = requests.get(url, headers=cls.__headers)
        return response

    @classmethod
    def post(cls, url, body):
        response = requests.post(url, json=body, headers=cls.__headers)
        return response

    @classmethod
    def put(cls, url, body):
        response = requests.get(url, json=body, headers=cls.__headers)
        return response

    @classmethod
    def delete(cls, url, body):
        response = requests.delete(url, json=body, headers=cls.__headers)
        return response
