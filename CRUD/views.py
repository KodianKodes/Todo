from django.shortcuts import render, redirect # make use of reques and render function
from django.http import HttpResponse
from .models import *  #importing all the model(classes) for my views
from .forms import *

# Create your views here.
def index(request):
    """Created a class 'crud' and call all the objects of crud for views page. """
    crud_model = Crud.objects.all()

    form = CrudForm() #declaration of form and assigning it to class model Crud.
    
    if request.method == "POST":
        form = CrudForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'display': crud_model,
         'form':form
         }
    return render(request, 'CRUD/index.html', context)

def update(request, pk):
    task = Crud.objects.get(id=pk)

    form = CrudForm(instance=task)

    if request.method == 'POST':
        form = CrudForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
     
    return render(request, 'CRUD/update_crud.html', context)


def delete(request, pk):
    item = Crud.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'CRUD/delete.html', context)
