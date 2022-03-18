from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class UserCreationFormExtended(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'password1', 'password2'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.object.filter(email=email).exists():
            raise forms.ValidationError(
                "Este correo electrónico ya fue registrado")

        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'avatar', 'occupation',
            'institution', 'bio'
        )

        widgets = {
            'avatar': forms.ClearableFileInput(
                attrs={'class': 'form-control-file mt-3'}
            ),
            'bio': forms.Textarea(
                attrs={
                    'class': 'form-control m-2',
                    'rows': 3,
                    'placeholder': 'Cuentanos lo genial que eres'}
            ),
            'link': forms.URLInput(
                attrs={
                    'class': 'form-control m-2',
                    'placeholder': 'https://mi-perfil.com'}
            )
        }
