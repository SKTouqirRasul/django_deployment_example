from django.conf.urls import url
from student_app import views

#app_name = 'student_app'

urlpatterns =[
    url(r'^student/$',views.student_view.as_view(), name='student'),
    url(r'^school/$',views.school_view.as_view(), name='school')


]
