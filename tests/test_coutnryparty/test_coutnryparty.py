import pytest

from utils.counterparty import Counterparty


@pytest.mark.counterparty
class TestCounterparty:
    @pytest.mark.counterparty
    @pytest.mark.positive
    @pytest.mark.parametrize('first_name', 'middle_name', 'last_name', 'phone', 'email', 'counterparty_type', 'c_property', [
        ("Іван", "Іванович", "Іванов", "380997979789", "test@i.com","PrivatePerson", "Recipient")
    ])
    def test_save_counter_party(self, first_name, middle_name, last_name, phone, email, counterparty_type, c_property):
        """
        Test
        """
        response_post = Counterparty.save_counter_party(first_name, middle_name, last_name, phone, email,
                                                        counterparty_type, c_property)
        assert response_post.json()['success'] is True
