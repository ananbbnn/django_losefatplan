from django.shortcuts import render

# Create your views here.

def home_page(request):
    """
    Render the home page.
    """
    return render(request, 'home/home_page.html')