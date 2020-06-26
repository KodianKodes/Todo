from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    crud_model = Crud.objects.all()

    form = CrudForm()

    if request.method == "POST":
        form = CrudForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect

    context = {
        'display': crud_model,
         'form':form
         }
    return render(request, 'CRUD/index.html', context)

 