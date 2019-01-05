from django.urls import path
from testapp import views
from testapp.apps import TestappConfig

app_name = 'testapp'
urlpatterns = [
    path('sport/', views.sport_news_View, name='sport')
]
