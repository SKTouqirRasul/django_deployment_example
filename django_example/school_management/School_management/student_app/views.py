from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,View
from student_app import models
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from student_app.forms import School_Form,Student_details_Form
# Create your views here.

class IndexView(TemplateView):
    template_name = 'homagpage.html'

class student_view(View):
    form_class = Student_details_Form
    template_name = 'student_details.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        return render(request,self.template_name,{'Student_details_Form':form})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Saved')

        return render(request,self.template_name,{'Student_details_Form':form})

class school_view(View):
    form_class = School_Form
    template_name = 'school.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name,{'School_Form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponse('data entered')

        return render(request, self.template_name,{'School_Form':form})
