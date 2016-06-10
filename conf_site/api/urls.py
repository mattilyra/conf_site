from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from . import views


# Create a router and register our viewsets with it.
router = SimpleRouter()
router.register(r'speaker', views.SpeakerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]