from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from workoutwarsapp.models import Team, Class


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    nick_name = forms.CharField(max_length=30, required=False, help_text='(if you have one)')
    email = forms.EmailField(max_length=254, required=True)
    team = forms.ModelChoiceField(queryset=Team.objects.all(), required=True,
            help_text='Check PQ Captains\' email for your assigned team')
    class_name = forms.ModelChoiceField(queryset=Class.objects.all(), required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'nick_name', 'email', 'class_name', 'team', 'password1', 'password2', )
