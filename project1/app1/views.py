# Create your views here.
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm
from .forms import Registrtion,RegistrtionForm



def regviews(request):
    form = UserRegistrationForm()
    template_name = 're.html'
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, template_name, context)


def loginviews(request):
    template_name = 'login.html'
    context = {}
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')

        user = authenticate(username=un, password=pw)

        if user is not None:
            login(request, user)
            return redirect('shop_url')
            
    return render(request, template_name, context)


def logoutviews(request):
    logout(request)
    return redirect('register_url')




def Registrview(request):
    template_name = 'reg.html'
   
    form1 = RegistrtionForm()
   
    if request.method == 'POST':
        form1 = RegistrtionForm(request.POST or None)
        if form1.is_valid():
            form1.save()
            return HttpResponse("Successfully Registered!!!")
    context = {'form1': form1}       
    return  render(request, template_name,context)