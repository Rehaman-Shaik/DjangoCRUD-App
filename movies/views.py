from django.shortcuts import render

# Create your views here.
def movies_home(request):
    context={}
    context['movies'] = "Movies homepage"
    return render(request, "movies_series/movies.html", context)