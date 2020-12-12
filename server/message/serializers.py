"""
Serializers module
"""
from rest_framework import serializers


class MessageOfTheDaySerialzier(serializers.Serializer):
    content = serializers.CharField(max_length=250)
    createdAt = serializers.DateTimeField()

