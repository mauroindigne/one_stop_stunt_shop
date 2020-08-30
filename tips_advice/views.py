from django.shortcuts import render

# Create your views here.


def view_tips_advice(request):
    """ A view to return the tips_advice page """
    return render(request, 'tips_advice/tips_advice.html')
