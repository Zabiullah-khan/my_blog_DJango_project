from django import forms

from django.contrib.auth.forms import User, UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm
 
from blogapp.models import NewsFeed

class SignupUser(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password1','password2']
		widgets={
			'username':forms.TextInput(attrs={'class':'form-control'}),
			'first_name':forms.TextInput(attrs={'class':'form-control'}),
			'last_name':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
		}

class LoginForm(AuthenticationForm):
	username = forms.CharField(error_messages={'required':'Enter Name'},widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	class Meta:
		model = User
		fields =['username','password']
		
class PostFeed(forms.ModelForm):
	class Meta:
		model = NewsFeed
		fields = ['title','postarea']
		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control'}),
			'postarea':forms.Textarea(attrs={'class':'form-control'}),
		}
		
class UserEditForm(UserChangeForm):
	password = None
	class Meta:
		model=User
		fields = ['username','first_name','last_name','email','date_joined','last_login','is_superuser','is_staff']
		widgets = {
			'username':forms.TextInput(attrs={'class':'form-control'}),
			'first_name':forms.TextInput(attrs={'class':'form-control'}),
			'last_name':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
			'date_joined':forms.DateInput(attrs={'class':'form-control'}),
			'last_login':forms.DateInput(attrs={'class':'form-control'}),
			
		}		

class PasswordEditForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	class Meta:
		model=User
		fields='__all__'

class ProfileEditForm(UserChangeForm):
	password = None
	class Meta:
		model=User
		fields=['username','first_name','last_name','email']
		widgets= {
			'username':forms.TextInput(attrs={'class':'form-control'}),
			'first_name':forms.TextInput(attrs={'class':'form-control'}),
			'last_name':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
		}
