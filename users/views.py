from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
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
        return redirect(reverse('home_page'))
    
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


def detail_view(request, id):
    context = {}
    profile = Profile.objects.get(id = id)
    print(f"profile: {profile}")
    print(profile.user_name)
    context['data'] = profile
    return render(request, 'curd_op/user_details.html', context)


def update_user(request, id):
    context = {}
    
    user = get_object_or_404(Profile, id=id)
    form = ProfileForms(request.POST or None, instance=user)
    
    if form.is_valid():
        form.save()
        return redirect(reverse('user_details', kwargs={'id': id}))
        #return HttpResponseRedirect("user/" + str(id))
    
    context['form'] = form
    context['id']=id
    return render(request, 'curd_op/update_user.html', context)

def delete_user(request, id):
    context={}
    context['id']=id
    profile = Profile.objects.get(id=id)
    if request.method =="POST":
        profile.delete()
        return redirect(reverse('list_all_users'))
    return render(request, 'curd_op/delete_user.html', context)


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


#def login(request):
#    return render(request, 'auth/login.html')