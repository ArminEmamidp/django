from django import forms


class CommentForm(forms.Form):
    user_name = forms.CharField(label='Name', max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'}))
    user_email = forms.EmailField(label='Email', max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your email'}))
    text = forms.CharField(max_length=1000, required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter your text'}))