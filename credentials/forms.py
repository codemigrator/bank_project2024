from django import forms
from . models import FromTable,Districts,Branch

class TableForm(forms.ModelForm):
    class Meta:
        model = FromTable
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={ 'placeholder': 'enter you name', 'class': 'form-control ', 'style': 'width:250px;'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control','style': 'width:250px;','type': 'date'}),
            'age': forms.NumberInput(attrs={'class': 'form-control','style': 'width:250px;'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control','style': 'width:250px;'}),
            'mail_id': forms.EmailInput(attrs={'class': 'form-control','style': 'width:250px;','type':'email'}),
            'address': forms.Textarea(attrs={'class': 'form-control','style': 'width:250px;'}),
            'district':forms.Select(attrs={'class':'form-control','style': 'width:250px;'}),
            'branch': forms.Select(attrs={'class': 'form-control','style': 'width:250px;'}),
            'account_type': forms.Select(attrs={'class': 'form-control','style': 'width:250px;'}),
            'choices': forms.CheckboxSelectMultiple(attrs={'class': 'checkboxes','style': 'float:left'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['branch'].queryset = Branch.objects.none()

            # if 'country' in self.data:
            #     try:
            #         country_id = int(self.data.get('country'))
            #         self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            #     except (ValueError, TypeError):
            #         pass  # invalid input from the client; ignore and fallback to empty City queryset
            # elif self.instance.pk:
            #     self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
