from django import forms

from cars.models import Cars

class CreateCarsForm(forms.ModelForm):

    class Meta:
        model = Cars
        fields = ['brand','model','year','color','price','condition','fuel_type','image']





class UpdateCarsForm(forms.ModelForm):

    class Meta:
        model = Cars
        fields = ['brand','model','price','image',]

    def save(self, commit=True):
        cars =  self.instance
        cars.brand  =   self.cleaned_data['brand']
        cars.model  =   self.cleaned_data['model']
        cars.price  =   self.cleaned_data['price']

        if self.cleaned_data['image']:
            cars.image  =   self.cleaned_data['image']
        if commit:
            cars.save()
        return cars

