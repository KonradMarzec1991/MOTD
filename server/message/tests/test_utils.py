
from datetime import datetime
from unittest.mock import patch, Mock

from message.serializers import MessageOfTheDaySerialzier
from message.utils import get_view_data


class TestCache:

    def test_if_key_is_none(self):
        with patch('message.utils.get_client_ip') as ip:
            with patch('message.utils.cache.get') as cache_get:
                with patch('message.utils.cache.set') as cache_set:
                    # cache.set is called, because cache.get(...) gets None
                    cache_get.return_value = None
                    get_view_data(
                        request=Mock(return_value='ip1'),
                        serializer_class=MessageOfTheDaySerialzier
                    )
                    cache_set.assert_called()

    def test_if_key_exists(self):
        with patch('message.utils.get_client_ip') as ip:
            with patch('message.utils.cache.get') as cache_get:
                with patch('message.utils.cache.set') as cache_set:
                    cache_get.return_value = {
                        'content': 'quote',
                        'created_at': datetime.utcnow()
                    }
                    # the value of IP itself is not important
                    get_view_data(
                        request=Mock(return_value='ip2'),
                        serializer_class=MessageOfTheDaySerialzier
                    )
                    # cache.get is not None, cache.set will not be called
                    cache_set.assert_not_called()
