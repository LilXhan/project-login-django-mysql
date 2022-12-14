from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SingUpUserForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    
    def save(self, commit=True):
        user = super(SingUpUserForm, self).save(commit=False)

        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        
        return user