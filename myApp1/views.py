#соединяет данные и шаблоны. Принимает http запросы и отправлчет http ответы

from django.shortcuts import render

#функция для отображения страницы index.html
def index_pade(request):    #http request (запрос) входит
#Здесь берем данные из БД какие надо отобразить на странице
#или что-тл подсчитываем и выполняем какие-либо действия
    return render(request, 'index.html')    #http response (ответ) выходит
