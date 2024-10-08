from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import the User model

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
