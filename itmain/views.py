# Импортируем функцию render для показа HTML-шаблонов
from django.shortcuts import render
# Импортировали бы HttpResponse для простого текста (сейчас не нужно)
#from django.http import HttpResponse

# Функция для главной страницы
def index(request):
    data = {
        'title': 'Главная страница',
        'values' :['Some','hello','1,2,3']
    }
    # Показываем пользователю шаблон index.html
    return render(request,'itmain/index.html',data)

# Функция для страницы about
def about(request):
    # Показываем пользователю шаблон about.html
    return render(request,'itmain/about.html')

