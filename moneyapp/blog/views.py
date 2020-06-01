from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'blog/home.html')
    
@login_required
def earning(request):
    return render(request, 'blog/earning.html')

