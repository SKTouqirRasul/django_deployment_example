from django.shortcuts import render
from django.urls import reverse

#def get_url():
#    return reverse('testapp:other')

# Create your views here.
def index_view(request):
    return render(request, 'testapp/index.html')

def home_view(request):

    return render(request, 'testapp/home.html' )


def other_view(request):

    return render(request, 'testapp/other.html')
