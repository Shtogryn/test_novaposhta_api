import pytest

from utils.counterparty import Counterparty


@pytest.mark.counterparty
@pytest.mark.skip
class TestCounterparty:
    @pytest.mark.parametrize('ref', [
        'ea712f78-a16d-11ed-a60f-48df37b921db'
    ])
    def test_get_street(self, ref):
        """
        Test
        """
        response_post = Counterparty.delete_counter_party(ref)
        assert response_post.json()['success'] is True
