from django import forms
from .models import Company
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name',
        ]


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'first_name',
            'last_name'
        ]


class UserEditForm(UserChangeForm):
    class Meta:
        model = User

        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'user_permissions',
            'is_superuser',
            'is_staff',
            'is_active'
        ]
