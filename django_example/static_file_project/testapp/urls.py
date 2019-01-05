from django.urls import path
from testapp import views
urlpatterns = [
    path('test/', views.date_view),
]
