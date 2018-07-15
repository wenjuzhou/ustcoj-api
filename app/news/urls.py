from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from news import views

router = DefaultRouter()
router.register(r'^news/', views.NewsViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
