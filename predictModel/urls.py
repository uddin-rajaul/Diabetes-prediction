from django.urls import path

# add this to import our views file
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('results/', views.result, name='result'),
]