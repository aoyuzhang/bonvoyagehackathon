from django.shortcuts import render
from .models import Restaurent,Food

# Create your views here.
# from .models import Board

def home(request):
  return render(request, 'base.html')

def resto(request):
  restaurents = Restaurent.objects.all()
  return render(request, 'restaurents.html', {'restos': restaurents})

def food(request):
  foods = Food.objects.all()
  return render(request, 'foods.html', {'foods': foods})


def addfood(request):
  return render(request,"addfood.html")