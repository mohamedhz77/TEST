from django import forms
from django .contrib.auth.models import User
from django .contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Profile

class RegisterUserForm(UserCreationForm):

    class Meta:
       model = User
       fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )

class UpdateUserForm(UserChangeForm):

    class Meta:
       model = User
       fields = ['first_name','last_name','email' ]
       
class UpdateProfileForm(UserChangeForm):

    class Meta:
       model = Profile
       fields = ('date_of_birth','photo' )
       

