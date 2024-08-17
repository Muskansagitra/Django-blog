
from tokenize import group
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views import View
from .form import SignupForm,PostForm,ContactForm
from .models import Contact, Post
from django.contrib.auth.models import Group
# from .form import RegistrationForm

# Create your views here.
# home
def home(request):
  posts = Post.objects.all()
  return render(request,'blog/home.html',{'posts':posts})
# about
def about(request):
  return render(request,'blog/about.html')  

# contact
def contact(request):
  if request.method == "POST":
     form=ContactForm(request.POST)
     if form.is_valid():
      name=form.cleaned_data['name']
      password=form.cleaned_data['password']
      address = form.cleaned_data['address']
      message = form.cleaned_data['message']
      cont = Contact(name=name,password=password,address=address,message=message)
      cont.save()
      form=ContactForm()  
  else:
    form=ContactForm()  
  return render(request,'blog/contact.html',{'form':form})
    
# dashboard
def dashbord(request):
  if request.user.is_authenticated:
   posts = Post.objects.all()
   user=request.user
   full_name=user.get_full_name()
   gps=user.groups.all()
   return render(request,'blog/dashbord.html',{'posts':posts,'user':user,'full_name':full_name,'groups':gps})
  else:
   return HttpResponseRedirect("login/")
  
# logout
def logout(request):  
    return redirect(request,'blog/login.html')
  
  
# signup
def signup(request):
  if request.method == "POST":
    form=SignupForm(request.POST)
    if form.is_valid():
     messages.success(request,"Congratulation, You have successfully Registered !!")
     user=form.save()
     group=Group.objects.get(name='Author')
     user.groups.add(group)              
  else:
    form=SignupForm()     
  return render(request,'blog/signup.html',{'form':form})


# edit
def edit(request,id):
  if request.user.is_authenticated:
    if request.method=='POST':
     update=Post.objects.get(pk=id)
     form=PostForm(request.POST,instance=update)
     if form.is_valid():
       form.save()

    else: 
      update=Post.objects.get(pk=id)
      form=PostForm(instance=update)
    return render(request,'blog/edit.html',{'form':form})
  else:
    return HttpResponseRedirect("/login/")
  
 # addpost
def add_post(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
       form = PostForm(request.POST)
       if form.is_valid():
         messages.success(request," Congratulations!! Your Post has add !!")

         title=form.cleaned_data['title']
         description=form.cleaned_data['description']  
         ap=Post(title=title,description=description)
         ap.save()  
         form=PostForm()
    else:
       form=PostForm()
    return render(request,'blog/addpost.html',{'form':form})
  else:
    return HttpResponseRedirect("/login/")
     


# delete
def delete(request,id):
  if request.user.is_authenticated:
    dele = Post.objects.get(id=id)
    dele.delete()
    return  HttpResponseRedirect('/dashbord/')
  else:
   return  HttpResponseRedirect('/login/')
    
