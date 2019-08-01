from django import forms

from personal.models import Contactus
from personal.models import Aja 

class CreateMsgForm(forms.ModelForm):


    class Meta:
        model = Contactus
        fields = ['email','phonenumber','message']





class CreateAjaForm(forms.ModelForm):

    class Meta:
        model = Aja
        fields = ['email','phonenumber']

