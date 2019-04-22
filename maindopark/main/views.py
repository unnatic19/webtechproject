from django.shortcuts import render
from .forms import LoginForm,detail_form
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, render
from .models import login

def profile_det(request):
    return render(request, 'profile_det.html')
def aboutus_new(request):
    return render(request, 'aboutus_new.html')
def features_new(request):
    return render(request, 'features_new.html')
def landing(request):
    return render(request, 'landing.html')
def maps(request):
    return render(request, 'maps.html')
def profile_new(request):
     return render(request, 'profile_new.html')

'''def profile_det(request):
    #p=login.objects.get()
    return render(request, 'profile_det.html')

'''
def results(request):
    posts = login.objects.get(username = request.user)
    return render(request, 'profile_det.html', {'posts': posts})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def error_404_view(request, exception):
    return render(request,'main/error404.html')



