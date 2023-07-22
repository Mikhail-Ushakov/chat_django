from django.urls import path
from .views import subscribe_view

urlpatterns = [
    path('subscribe/<int:pk>/', subscribe_view, name='subscribe'),
]