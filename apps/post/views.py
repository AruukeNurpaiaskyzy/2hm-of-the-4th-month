from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.
def hello(request):
    return HttpResponse("Hello World!")

def direction(request):
    return HttpResponse("Backend (Python/Django)")

def test(request):
    return render(request, 'test.html')

def about(request):
    context = {
        'title': "О нас",
        'description': "Мы группа 18-1B ",
        'students': ['Митаева Кызжибек', 'Нурпаяз кызы Арууке', 'Анвардинов Билолдин', 'Анапияев Залкар']
    }
    return render(request, 'about.html', context)

def news(request):
    context = {
        'title': "новости",
        'news': "сегодня машина сбила человека"
    }
    return render(request, 'news.html', context)
def contacts(request):
    context = {
        'contacts': 7786787787667
    }
    return render(request, 'contact.html', context)
def currentt(request):
    time = timezone.now()
    context = {

        'currentt': time.strftime('%Y-%m-%d')
    }
    return render(request, 'currentt.html', context)





   
