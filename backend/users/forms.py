from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import User
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model= User 
        fields="__all__"
        error_class="error"
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model= User 
        fields= "__all__"
        error_class="error"
    