# appname/forms.py

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from registration.forms import RegistrationFormUniqueEmail

from SSIR_auth.models import CustomUser

class CustomUserCreationForm(RegistrationFormUniqueEmail):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)

    class Meta:
        model = CustomUser
        fields = ('business_name', 'email', 'work_phone')

class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)

    class Meta:
        model = CustomUser
        fields = ('business_name', 'email', 'work_phone')