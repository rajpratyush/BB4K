from django.shortcuts import render, redirect
from .forms import KidRegisterForm, ParentRegisterForm

# Create your views here.
def homepage_view(request, *args, **kwargs):
    context = {}
    return render(request, " ", context)



def kid_register_view(response, *args, **kwargs):
    if response.method == "POST":
        form = KidRegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect(" ")
        else: 
            form = ParentRegisterForm()

        return render(response, " ", { 'form': form})

def parent_register_view(response, *args, **kwargs):
    if response.method == "POST":
        form = ParentRegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect(" ")
        else: 
            form = ParentRegisterForm()

        context = { 'form': form}
        return render(response, " ", context)


def kid_app_view(request, *args, **kwargs):
    context = {}
    return render(request, " ", context)

def parent_app_view(request, *args, **kwargs):
    context = {}
    return render(request, " ", context)


