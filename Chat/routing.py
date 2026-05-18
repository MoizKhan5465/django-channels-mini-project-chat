from django.urls import re_path

from . import consumer

websocket_urlpatterns=[
    # Accept any room name that does not include a slash.
    # This allows spaces and percent-decoded names like 'friends group'.
    re_path(r'ws/chat/(?P<room_name>[^/]+)/$', consumer.ChatConsumer.as_asgi()),
]