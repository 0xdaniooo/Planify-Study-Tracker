from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    # Override the default form field attributes
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Choose a unique username'
        self.fields['password1'].help_text = '<ul><li>Must contain at least 8 characters.</li><li>Cannot be a commonly used password.</li><li>Cannot be entirely numeric.</li></ul>'
        self.fields['password2'].help_text = 'Repeat your password'

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class EditAccountForm(UserChangeForm):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = None

    class Meta:
        model = User
        fields = ('username', 'email')


class PasswordDataChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].help_text = '<ul><li>Must contain at least 8 characters.</li><li>Cannot be a commonly used password.</li><li>Cannot be entirely numeric.</li></ul>'
        self.fields['new_password2'].help_text = 'Repeat your password'

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')