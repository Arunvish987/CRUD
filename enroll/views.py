from django.shortcuts import render, redirect
from . forms import UserForm
from . models import User

# Create your views here.
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        form = UserForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = User.objects.get(pk=id)
        form = UserForm(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':form})

def add_show(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']

        reg = User(name=nm, email=em, password=pw)
        reg.save()
        form = UserForm()

    else:
        form = UserForm()

    std = User.objects.all()
        
    return render(request, 'enroll/addandshow.html', {'form':form, 'std':std})

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('/')

