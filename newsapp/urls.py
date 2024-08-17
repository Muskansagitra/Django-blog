
from django.contrib import admin
from django.urls import path
from newsapp import views
from django.contrib.auth import views as auth_views

from newsapp.form import LoginForm

urlpatterns = [
   path('',views.home,name="home"),
   path('about/',views.about,name="about"),
   path('contact/',views.contact,name="contact"),
   path('dashbord/',views.dashbord,name="dashbord"),
   path('login/',auth_views.LoginView.as_view(template_name='blog/login.html',form_class=LoginForm),name="login"),
   path('signup/',views.signup,name="signup"),
   path('logout/',auth_views.LogoutView.as_view(),name="logout"),
   path('edit/<int:id>/',views.edit,name='edit'),
   path('delete/<int:id>/',views.delete,name='delete'),
   path('addpost/',views.add_post,name="addpost")
   
#    path('registration/',views.Registrationview.as_view(),name="registration")
]
