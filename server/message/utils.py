"""
Helper functions module
"""
from django.core.cache import cache

from .models import MessageOfTheDay


def get_client_ip(request):
    """Gets IP of given request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_view_data(request, serializer_class):
    """
    Retrieves from cache view content or creates it using `MessageOfTheDay`
    :param request: request object (from view)
    :param serializer_class: name of serializer
    :return: validated dict with quote and timestamp
    """
    ip = get_client_ip(request)
    cached_ip_value = cache.get(ip, None)
    if cached_ip_value:
        serializer = serializer_class(data=cached_ip_value)
    else:
        serializer = serializer_class(data=MessageOfTheDay().to_dict())
    serializer.is_valid(raise_exception=True)
    return serializer.data
