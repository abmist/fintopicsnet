from django.shortcuts import render

def about_map(request):
    return render(request, "about/about.html")




"""
def about_info(request):
    return render(request, "about/about.html", {'info': "This is about information."})
"""