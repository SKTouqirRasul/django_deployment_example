from django import forms
from testapp.models import SimpleModel


class Simple_Form(forms.Form):
    name= forms.CharField(max_length=60)
    email=forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
# this filed to will be hidden and in the user form and and will help to identyfy if any bot tried to filled the form
    botcaher = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_botcaher(self):
        botcaher= self.cleaned_data['botcaher']
        if len(botcaher)>0:
            raise forms.ValidationError('a bot tring to fill the from')


    def clean_name(self):
        name=self.cleaned_data['name']
        if name=='admin':
            raise forms.ValidationError('name can not be admin')
        if len(name)>64:
            forms.ValidationError('name can not be more than 64 characters')
        return name


    def clean_email(self):
        email=self.cleaned_data['email'].lower()
        r= SimpleModel.objects.filter(email=email)
        if r.count:
            raise forms.ValidationError("{0} already exists".format(email))

        return email.lower()



    def save(self):
        simple_m = SimpleModel.objects.create(
            name =self.cleaned_data['name'],
            email = self.cleaned_data['email'],
            text= self.cleaned_data['text']
             )
