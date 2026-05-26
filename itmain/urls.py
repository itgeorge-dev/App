# Импортируем функцию path для создания маршрутов
from django.urls import path
# Импортируем представления (функции) из текущего приложения
from . import views

# Список всех URL-адресов сайта (маршрутов)
urlpatterns = [
    # Главная страница сайта (путь без адреса) → вызывает функцию index из views
    path('', views.index,name='home'),

    # Страница "О нас" (адрес /about) → вызывает функцию about из views
    path('about', views.about,name='about'),
]