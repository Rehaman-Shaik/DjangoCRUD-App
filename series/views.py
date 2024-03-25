from django.shortcuts import render

# Create your views here.

def series_home(request):
    context={}
    context['series'] = "Series homepage"
    return render(request, "movies_series/series.html", context)