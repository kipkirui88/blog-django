from django.shortcuts import render
from .models import news

# Create your views here.
def index(request):
    context ={
        "news": news.objects.all()
    }
    return render (request, 'index.html', context)
