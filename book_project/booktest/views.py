from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import BookInfo,HeroInfo


def index(request):
    books = BookInfo.objects.all()
    a1 = BookInfo.objects.filter(id=1)
    return render(request, 'index.html', {"books": books, "a1": a1})


def hero(request, book_id):
    heros = HeroInfo.objects.filter(hbook=book_id)
    return render(request, 'hero.html', {"heros": heros})
