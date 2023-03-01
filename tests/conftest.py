import pytest


@pytest.fixture()
def data_search_settlements():
    return [
        ('Київ', 5, 1),
        ('Львів', 7, 1),
        ('Харків', 3, 1)
    ]
