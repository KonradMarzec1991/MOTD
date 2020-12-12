"""
Serializers module
"""
from rest_framework import serializers


class MessageOfTheDaySerialzier(serializers.Serializer):
    """
    Serializes fields of MessageOfTheDay model
    """
    content = serializers.CharField(max_length=250)
    created_at = serializers.DateTimeField()
