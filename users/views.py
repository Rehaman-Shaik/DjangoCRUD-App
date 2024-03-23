from django.shortcuts import render
#from django.http import HttpResponse
from .models import Profile
from .forms import ProfileForms
# Create your views here.

def landing_page(request):
    return render(request, 'landing_home.html')

def add_users(request):
    context = {}
    form =  ProfileForms(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, 'curd_op/add_user_page.html', context)
    #return render(request, 'curd_op/add_user_page.html')
    
def list_all_users(request):
    context = {}
    profiles = Profile.objects.all()
    context['dataset']= profiles
    context['length'] = len(profiles)
    return render(request, 'curd_op/list_all_users.html', context)

def home_page(request):
    return render(request, 'home.html')
    