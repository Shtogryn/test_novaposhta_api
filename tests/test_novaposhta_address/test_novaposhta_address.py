import pytest
from utils.address import Address
from utils.http_methods import HttpMethods

import pytest


@pytest.mark.addresses
class TestAddress:

    @pytest.mark.positive
    @pytest.mark.parametrize('city_name, limit, page', [
        ('Київ', 5, 1),
        ('Львів', 7, 1),
        ('Харків', 3, 1),
    ])
    def test_search_settlements(self, city_name, limit, page):
        """
        Positive test online settlements searching
        """
        response_post = Address.search_settlements(city_name, limit, page)
        assert response_post.json()['success'] is True
        assert response_post.json()['data'][0]['Addresses'][0]['MainDescription'] == city_name
        res_list = response_post.json()['data'][0]['Addresses']
        is_main_description = [True if i['MainDescription'] != '' else False for i in res_list]
        assert is_main_description
        assert len(response_post.json()['data'][0]['Addresses']) >= 1

    @pytest.mark.negative
    @pytest.mark.parametrize('city_name, limit, page', [
        ('Kyiv', 3, 1),
        ('_Київ', 5, 1),
        ('Тернoпiль', 5, 1),
        ('Львів', 7, -1),
        ('Київ', 0, 1)
    ])
    def test_negative_search_settlements(self, city_name, limit, page):
        """
        Negative test online settlements searching
        """
        response_post = Address.search_settlements(city_name, limit, page)
        if limit > 0 and page > 0:
            assert response_post.json()['success'] is False
            assert response_post.json()['errors'][0] == 'CityName has invalid characters'
        elif page < 0:
            assert response_post.json()['success'] is False
            assert response_post.json()['errors'][0] == 'Page is not specified'
            assert response_post.json()['errorCodes'] == ['20000400474']
        else:
            assert response_post.json()['success'] is True
            assert response_post.json()['errors'] == []
            assert response_post.json()['errorCodes'] == []

    @pytest.mark.positive
    @pytest.mark.parametrize('ref, find_by_string, limit', [
        ('8d5a980d-391c-11dd-90d9-001a92567626', 'Київ', 5)
    ])
    def test_get_cities(self, ref, find_by_string, limit):
        """
        Test get cities information
        """
        response_post = Address.get_cities(ref, find_by_string, limit)
        assert response_post.json()['success'] is True
        assert response_post.json()['data'][0]['Description'] == find_by_string

    @pytest.mark.skip
    @pytest.mark.parametrize('ref, find_by_string, limit, page', [
        ('8d5a980d-391c-11dd-90d9-001a92567626', 'Київ', 5, 1)
    ])
    def test_get_street(self, ref, find_by_string, limit, page):
        """
        Test get streets information
        """
        response_post = Address.get_cities(ref, find_by_string, limit)
        assert response_post.json()['success'] is True
        assert response_post.json()['data'][0]['Description'] == find_by_string

    @pytest.mark.skip
    def test_delete_item(self, api_url, item_to_delete):
        """
        Test online settlements searching
        """
        response = HttpMethods.delete(api_url, {"apiKey": "7c2f707c25bfe0147cdf6c2330e494bd",
                                                "modelName": "InternetDocument",
                                                "calledMethod": "delete",
                                                "methodProperties": {"DocumentRefs": [item_to_delete]}})
        assert response.json()["success"] is True
