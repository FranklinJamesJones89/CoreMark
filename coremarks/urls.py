from django.urls import path

from . import views

app_name = 'coremarks'
urlpatterns = [
    path('', views.index, name='index'),
    path('day/<int:pk>/', views.day_detail, name='day_detail'),

]
