import pytest

from utils.counterparty import Counterparty


class TestCounterparty:
    @pytest.mark.counterparty
    @pytest.mark.positive
    def test_save_counter_party(self):
        """
        Test
        """
        response_post = Counterparty.save_counter_party("Іван", "Іванович", "Іванов", "380997979789", "test@i.com",
                                                        "PrivatePerson", "Recipient")
        assert response_post.json()['success'] is True
