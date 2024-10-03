from django import forms
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from ..models import Profile

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model= User
        fields = ['username', 'password', 'password_confirm']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'todo:register'
        self.helper.add_input(Submit('submit', 'Register'))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        #check if passwords match
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'todo:login'
        self.helper.add_input(Submit('submit', 'Login'))

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['date_of_birth', 'profile_picture']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}, format=('%d/%m/%Y')),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'