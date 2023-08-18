from django.contrib.auth.models import User
from django import forms
from .models import Record


class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control my-3"}
        ),
    )

    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control my-3",
            }
        ),
    )
    password_confirm = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "form-control my-3",
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password_confirm",
        )


class PostForm(forms.ModelForm):
    first_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    address = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Address"}
        ),
    )
    city = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "City"}),
    )

    zipcode = forms.IntegerField(label="")

    class Meta:
        model = Record
        fields = ("first_name", "last_name", "address", "city", "zipcode")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["zipcode"].widget.attrs["class"] = "form-control"
        self.fields["zipcode"].widget.attrs["placeholder"] = "Zip code"
