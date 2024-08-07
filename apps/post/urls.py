from django.urls import path

from apps.post.views import hello, direction, test, about, news, contacts, currentt

urlpatterns = [
    path('hi/', hello),
    path('dir/', direction),
    path('test/', test),
    path('about/', about, name="about"),
    path('news/', news, name="news"),
    path('con/', contacts, name="contacts"),
    path('cur/', currentt, name="currentt"),
]
