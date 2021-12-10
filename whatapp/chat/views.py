from django.shortcuts import render

# Create your views here.igra
from django.shortcuts import render

def index(request):
    return render(request,'index.html')