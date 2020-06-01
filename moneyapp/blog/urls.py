from django.urls import path
from .views import home, earning

urlpatterns = [
    path('', home, name='home'),
    path('earning/', earning, name='earning'),
]