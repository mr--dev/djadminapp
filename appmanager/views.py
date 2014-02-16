from django.shortcuts import render
from appmanager.models import App

# Create your views here.

def index(request):

    apps = App.objects.all()
    ctx = {'apps': apps}
    return render(request, 'appmanager/index.html', ctx)
