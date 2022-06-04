from django.shortcuts import render
# from django.http import HttpResponse
from . models import SearchLog
from . raw_query import raw_query

# Create your views here.


def home(request):
    AroVar = {"alpha": "A", "bita": "B", "gamma": 'C'}
    return render(request, 'aro_app/home.html', {"AroVar": AroVar})


def about(request):
    GetInfo = SearchLog.objects.all()
    return render(request, 'aro_app/about.html', {"GetInfo": GetInfo})


def contact(request):
    commodities = raw_query("SELECT * FROM `commodities`")
    return render(request, 'aro_app/contact.html', {"commodities": commodities})
