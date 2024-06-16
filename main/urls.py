from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('registration', views.registration, name='registration'),
    path('user', views.user, name='user'),
    path('attractions', views.attractions, name='attractions'),
    path('route', views.route, name='route'),
]