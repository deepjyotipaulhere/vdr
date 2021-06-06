from django.shortcuts import render
from .models import FileSubcategory, Files

# Create your views here.


def index(request):
    return render(request, 'web/index.html', {'data': Files.objects.all(), 'items': FileSubcategory.objects.all()})
