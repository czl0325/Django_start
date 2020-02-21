from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import BookInfo,HeroInfo
from datetime import date
from django.db.models import F, Q, Sum, Count, Avg, Max, Min


def index(request):
    books = BookInfo.objects.all()

    a1 = BookInfo.objects.filter(id=1)
    a2 = BookInfo.objects.filter(btitle__contains='传')
    a3 = BookInfo.objects.filter(btitle__endswith='部')
    a4 = BookInfo.objects.filter(btitle__isnull=False)
    a5 = BookInfo.objects.filter(id__in=[1, 3, 5])

    b1 = BookInfo.objects.filter(id__gt=3)
    b2 = BookInfo.objects.exclude(id=3)
    b3 = BookInfo.objects.filter(bpub_date__year=1980)
    b4 = BookInfo.objects.filter(bpub_date__gt=date(1980, 1, 1))

    c1 = BookInfo.objects.filter(bread__gt=F('bcomment'))
    c2 = BookInfo.objects.filter(bread__gt=F('bcomment')*2)

    d1 = BookInfo.objects.filter(Q(bread__gt=20) & Q(id__lt=3))
    d2 = BookInfo.objects.filter(~Q(id=3))

    e1 = BookInfo.objects.aggregate(Sum('bread'))
    e2 = BookInfo.objects.count()

    f1 = BookInfo.objects.filter(heroinfo__hcomment__contains='八')
    f2 = HeroInfo.objects.filter(hbook__btitle='天龙八部')

    return render(request, 'index.html', {"books": books, "a1": a1, "a2": a2, "a3": a3, "a4": a4, "a5": a5, "b1": b1, "b2": b2, "b3": b3, "b4": b4, "c1": c1, "c2": c2, "d1": d1, "d2": d2, "e1": e1, "e2": e2, "f1": f1, "f2": f2})


def hero(request, book_id):
    heros = HeroInfo.objects.filter(hbook=book_id)
    return render(request, 'hero.html', {"heros": heros})



