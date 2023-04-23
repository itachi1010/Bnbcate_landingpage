from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



app_name = 'landing_page'

urlpatterns = [
    path('', views.index, name='index')
]
