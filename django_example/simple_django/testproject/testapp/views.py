from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def template_view(request):
    date =datetime.datetime.now()
    #s='<h1>the current datetime in the server is' + str(date)+ '</h1>'
    name='touqir'
    empid =32392
    my_dict={'name':name,'empid':empid}
    return render(request, 'testapp/result.html',context=my_dict)
