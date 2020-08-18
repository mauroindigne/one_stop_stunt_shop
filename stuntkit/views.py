from django.shortcuts import render

# Create your views here.

def view_stuntkit(request):
    """ A view to return the stuntkit page """
    return render(request, 'stuntkit/stuntkit.html')
