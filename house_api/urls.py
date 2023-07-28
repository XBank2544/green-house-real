from rest_framework import routers
from django.urls import include, path
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api/update/', views.updateSchedule)
]
