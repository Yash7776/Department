from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views  # Adjust based on your setup

urlpatterns = [
    # Your existing URL patterns
    path('login/<str:org>', views.login, name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)