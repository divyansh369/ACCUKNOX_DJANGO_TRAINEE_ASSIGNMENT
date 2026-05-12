from django.urls import path
from .views import test_signal

urlpatterns = [
    path("test/", test_signal),
]