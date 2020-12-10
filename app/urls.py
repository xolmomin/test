from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path
from rest_framework import routers

from app.views import NewViewSet

router = routers.DefaultRouter()
router.register(r'new', NewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('i18n/', include('django.conf.urls.i18n'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
