from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from .models import Post,Contact

class SignupForm(UserCreationForm):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={"class":"form-control"}))
    firstname = forms.CharField(label="First Name",widget=forms.TextInput(attrs={"class":"form-control"}))
    lastname = forms.CharField(label="Last Name",widget=forms.TextInput(attrs={"class":"form-control"}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={"class":"form-control"}))
   
class Meta:
    model = User
    fields = ['firstname','lastname','username','email','password']
    
    
class LoginForm(AuthenticationForm):
    username = UsernameField(label="UserName",widget=forms.TextInput(attrs={'class':'form-control'}))  
    password = forms.CharField(label=_("Password"),widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
class PostForm(forms.ModelForm):
 class Meta:
    model = Post
    fields =  ["title","description"]
    labels = {"title":"Title","description":"Description"}
    widgets = {"title":forms.TextInput(attrs={"class":"form-control"}),
               "description":forms.Textarea(attrs={"class":"form-control"})}
    
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact 
        fields = ["name","password","address","message"]
        labels = {"name":"Name","password":"Password","address":"Address","message":"Message"} 
        widgets = {"name":forms.TextInput(attrs={"class":"form-control"}),"password":forms.PasswordInput(attrs={"class":"form-control"}),"address":forms.TextInput(attrs={"class":"form-control"}),"message":forms.TextInput(attrs={"class":"form-control"})}  
    