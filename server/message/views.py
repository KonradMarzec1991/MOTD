# pylint: disable=unused-argument
"""
API Views module
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.renderers import JSONRenderer, HTMLFormRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer
from rest_framework_msgpack.renderers import MessagePackRenderer

from .serializers import MessageOfTheDaySerialzier
from .utils import get_view_data
from .renderer import PlainTextRenderer


class MessageView(APIView):
    """
    Displays Message of the day (MOTD)

    For example, the /etc/motd is a file on Unix-like systems that contains a
    "message of the day", used to send a common message to all users in a
    more efficient manner than sending them all an e-mail message.

    Possible content types of response:
    - JSON
    - Plain text
    - XML
    - YAML
    - MessagePack
    - HTML Form
    """
    def get(self, request):
        print(request.META.get('HTTP_ACCEPT'))
        data = get_view_data(request, MessageOfTheDaySerialzier)
        return Response(data, status=status.HTTP_200_OK)
