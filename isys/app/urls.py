from django.urls import path

from app.views import MessagesListView

urlpatterns = [
    path('', MessagesListView.as_view(), name='messages-list'),
]