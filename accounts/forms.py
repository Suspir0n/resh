from django import forms


class LoginForms(forms.Form):
    name_or_email_login = forms.CharField(
        label='Username or Email',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex. João Silva / joãosilva@resh.com'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Type your password'
            }
        )
    )


class SignupForms(forms.Form):
    name_signup = forms.CharField(
        label='Name',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex. João Silva'
            }
        )
    )

    username_signup = forms.CharField(
        label='Username',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex. joaosilva'
            }
        )
    )

    email = forms.EmailField(
        label='E-mail',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex. joãosilva@resh.com'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        required=True,
        max_length=70,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Type your password'
            }
        )
    )
    confirm_password = forms.CharField(
        label='Confirm your password',
        required=True,
        max_length=70,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password again'
            }
        )
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError('The passwords are not the same!')
            else:
                return confirm_password