from django.urls import path, include

from .views import UserSerializerViewSets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'user', UserSerializerViewSets)

urlpatterns = [
    
    path('' , include(router.urls))
    
]
