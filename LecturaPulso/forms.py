from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BootsrapStylesMixin:
    field_names = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.field_names:
            for fieldname in self.field_names:
                self.fields[fieldname].widget.attrs = {'class': 'form-control'}
        else:
            raise ValueError('The field_names must be set')


class  MyPassResetForm(BootsrapStylesMixin, PasswordResetForm):
    field_names = ['email']


class MySetPassForm(BootsrapStylesMixin, SetPasswordForm):
    field_names = ['new_password1', 'new_password2']

