from django.urls import path
from testapp import views

app_name='testapp'

urlpatterns=[
         path('home/', views.home_view,name='home'),
         path('other/', views.other_view,name='other')
]
