from django.contrib.auth.models import User
from django import forms


class UserInformationUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)


