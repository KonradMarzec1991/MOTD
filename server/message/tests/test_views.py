import pytest

from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework import status


class TestMessageView:

    @pytest.mark.parametrize('response_format, response_status', [
        ('application/json', status.HTTP_200_OK),
        ('text/plain', status.HTTP_200_OK),
        ('application/yaml', status.HTTP_200_OK),
        ('application/xml', status.HTTP_200_OK),
        ('application/msgpack', status.HTTP_200_OK),
        ('text/html', status.HTTP_406_NOT_ACCEPTABLE),
    ])
    def test_content_type(self, response_format, response_status):
        client = APIClient()
        response = client.get(
            reverse('motd-message'),
            HTTP_ACCEPT=response_format
        )
        assert response.status_code == response_status
