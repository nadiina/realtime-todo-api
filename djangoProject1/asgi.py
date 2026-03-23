import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject1.settings')

# Ініціалізуємо стандартний Django додаток
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
# AllowedHostsOriginValidator більше не імпортуємо
from realtime import routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    # Прибрали AllowedHostsOriginValidator, залишили тільки AuthMiddlewareStack
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})