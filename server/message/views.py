# pylint: disable=unused-argument
"""
API Views module
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import MessageOfTheDay
from .serializers import MessageOfTheDaySerialzier


class MessageView(APIView):
    """
    Displays Message of the day (MOTD)

    The /etc/motd is a file on Unix-like systems that contains a
    "message of the day", used to send a common message to all users in a
    more efficient manner than sending them all an e-mail message.
    """
    def get(self, request):
        serializer = MessageOfTheDaySerialzier(data=MessageOfTheDay().to_dict())
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
