"""
API Views module
"""
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import MessageOfTheDay
from .serializers import MessageOfTheDaySerialzier


class MessageView(APIView):

    def get(self, request):
        serializer = MessageOfTheDaySerialzier(data=MessageOfTheDay().to_dict())
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
