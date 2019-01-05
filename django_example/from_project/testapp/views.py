from django.shortcuts import render
from testapp.forms import Simple_Form
from django.http import HttpResponse
# Create your views here.

def index_view(request):

    return render(request, 'testapp/index.html')

def form_view(request):
    form = Simple_Form()

    if request.method=='POST':
        form = Simple_Form(request.POST)

        if form.is_valid():
            print('from data')
            print('NAME: '+form.cleaned_data['name'])
            print('EMAIL: '+form.cleaned_data['email'])
            print('text: '+form.cleaned_data['text'])
# this save method is the one we have defined in the forms.py file
            form.save()
            return HttpResponse('thanks for sumbitting the form')

    return render(request, 'testapp/form_page.html', {'form':form})
