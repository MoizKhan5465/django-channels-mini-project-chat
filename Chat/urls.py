

from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/chat/
    path('', views.lobby, name='lobby'),

    # http://localhost:8000/chat/friends/
    # <str:room_name> captures "friends"
    # passes it to views.room()
    path('<str:room_name>/', views.room, name='room'),
]