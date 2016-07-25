from django.shortcuts import render

def about_map(request):
    return render(request, "about/about.html")
