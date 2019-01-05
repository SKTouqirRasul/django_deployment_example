from django.shortcuts import render

# Create your views here.
def home_page_view(request):

    return render(request, 'testapp/homepage.html')


def sport_news_View(request):

    n1='virat is no more indian captain'
    n2='Rohit is the new indian ODI captain'

    return render(request, 'testapp/sport.html',{'n1':n1,'n2':n2})
