import os
import django

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.http import AsgiHandler
import api.routing
os.environ.setdefault("DJANGO_SETTINGS_MODULE","realtime_chat.settings")
django.setup()
application=ProtocolTypeRouter({
    "http":AsgiHandler(),
    "websocket":AuthMiddlewareStack(
        URLRouter(
            api.routing.websocket_urlpatterns
        )
    )
})