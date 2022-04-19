from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Gebruikersnaam",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Gebruikersnaam",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        label="Wachtwoord",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Wachtwoord",
                "class": "form-control"
            }
        ))