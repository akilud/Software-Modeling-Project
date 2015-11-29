from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=24, widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'style':'width:100%','class':'form-control'}))


class RegistrationForm(forms.Form):

    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    first_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'autofocus': 'autofocus', 'class':'form-control','style':'width:50%'}))
    last_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'style': 'width:100%', 'class': 'form-control'}))
    address = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'style': 'width:100%', 'class': 'form-control'}))
    zipcode = forms.CharField(max_length=5,widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:100%'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={'style': 'list-style-type:none'}), choices=GENDER_CHOICES)
    e_mail = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:100%'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:100%'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width:100%'}))

