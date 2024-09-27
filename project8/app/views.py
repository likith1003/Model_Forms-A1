from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
# Create your views here.


def register(request):
    EDFO = DataForm()
    d = {'EDFO': EDFO}
    if request.method == 'POST':
        o1 = DataForm(request.POST)
        if o1.is_valid():
            o1.save()
            return HttpResponse('Done....')
        return HttpResponse('Invalid Data')
    return render(request, 'register.html', d)