from django.shortcuts import render

# Create your views here.

def view_stuntkit(request):
    """ A view to return the stuntkit page """
    return render(request, 'stuntkit/stuntkit.html')


def view_basic_stuntkit_detail(request):
    """ A view to return the stuntkit page """
    return render(request, 'stuntkit/basic_stuntkit_detail.html')


def view_full_stuntkit_detail(request):
    """ A view to return the stuntkit page """
    return render(request, 'stuntkit/full_stuntkit_detail.html')