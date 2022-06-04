from django.shortcuts import render
# from django.http import HttpResponse
from . models import SearchLog
from . utility import layout
from . raw_query import raw_query

# Create your views here.


def home(request):
    AroVar = {"alpha": "A", "bita": "B", "gamma": 'C'}
    GetInfo = SearchLog.objects.all()
    commodities = raw_query("SELECT * FROM `commodities`")
    return layout(request, 'home.html', {"GetInfo": GetInfo, "AroVar": AroVar, "commodities": commodities})

    # return layout(request, 'home.html', AroVar)
    # return render(request, 'layout.html')
