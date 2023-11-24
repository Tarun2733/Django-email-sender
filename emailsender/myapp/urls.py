from django.urls import path
from .views import send_email, success, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('send-email/', send_email, name='send_email'),
    path('success/', success, name='success'),
]
