from pyexpat import model
from django import forms
from formmodel_app.models import Adress


class UserForm(forms.ModelForm):

    class Meta():

        model = Adress
        fields = '__all__'

