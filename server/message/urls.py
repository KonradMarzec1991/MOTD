from django.urls import path
from .views import MessageView

urlpatterns = [
    path('motd/', MessageView.as_view(), name='motd-message')
]
