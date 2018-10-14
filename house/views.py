from django.shortcuts import render
from django.views import generic
from .models import House
# Create your views here.

def index(request):
        house_list=House.objects.all()
        return render(request,'index.html',{'house_list':house_list})
