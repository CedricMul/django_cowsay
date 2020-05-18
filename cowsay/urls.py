from cowsay import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('history/', views.historyPage)
]