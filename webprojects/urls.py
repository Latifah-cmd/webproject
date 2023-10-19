from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home_page'),
    path('aboutus/', views.aboutus_view, name='aboutus_page'),
]