import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routing import websocket_urlpatterns  # Ensure correct import

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # ✅ Ensure this is a callable function
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
            )  # ✅ Ensure this is a list, not a tuple
    ),
})
