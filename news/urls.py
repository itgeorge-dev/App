# Импортируем функцию path для создания маршрутов
from django.urls import path
# Импортируем представления (функции) из текущего приложения
from . import views

# Список всех URL-адресов сайта (маршрутов)
urlpatterns = [
 path('', views.news_home , name='news'),
 path('create', views.create, name='create')
]
