from django.urls import path
from testapp import views

app_name='testapp'

urlpatterns = [

        path('register/',views.register,name='register'),
        path('user_login', views.user_login, name='user_login')

]
