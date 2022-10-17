from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,VehicleModel

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_superuser', 'is_admin', 'is_user')




class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class VehicleForm(forms.ModelForm):

    vehicle_number = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter Vehicle Number',
                                                               'class': 'form-control',
                                                               }))

    vehicle_model = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter Vehicle Number',
                                                               'class': 'form-control',
                                                               }))

            


    class Meta:
        model = VehicleModel
        fields = '__all__'

        CHOICES = (
        ('TWO_WHEELER', '2'),
        ('THREE_WHEELER', '3'),
        ('FOUR_WHEELER', '4')
        )
        widgets = {
            'Vehicle_type': forms.Select(choices=CHOICES,attrs={'class': 'form-control'}),
            'vehicle_description':forms.Textarea(attrs={'cols':30, 'rows': 6,'class': 'form-control'}),
        }