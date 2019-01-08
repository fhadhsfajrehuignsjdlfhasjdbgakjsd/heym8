from django import forms


class SignUpForm(forms.Form):

    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':"Username"
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email',
            }
        )
    )

    password = forms.CharField(
        max_length=128, 
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password'
            }
        ), 
    )


class SignInForm(forms.Form):

    Email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email',
            }
        )
    )

    Password = forms.CharField(
        max_length=128, 
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password'
            }
        ), 
    )

    RememberMe = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        )
    )
