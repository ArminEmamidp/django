from django import forms


class StudentCreateUpdateForm(forms.Form):
    first_name = forms.CharField(label='First Name', required=True, max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter first-name...'}))
    last_name = forms.CharField(label='Last Name', required=True, max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter last-name...'}))
    code = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter code...'}))

