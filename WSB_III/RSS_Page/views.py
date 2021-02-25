from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'RSS_Page/dashboard.html')

def zaplecze(request):
    return render(request, 'RSS_Page/zaplecze.html')