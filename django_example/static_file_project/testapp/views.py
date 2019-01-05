from django.shortcuts import render
import datetime
# Create your views here.
def date_view(request):
    date=datetime.datetime.now()
    h= int(date.strftime('%H'))
    return render(request, 'testapp/result.html', {'hour':h})
