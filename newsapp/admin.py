from django.contrib import admin
from .models import Contact, Post

# Register your models here.
@admin.register(Post)
class PostModelsAdmin(admin.ModelAdmin):
    list_dist=['id','title',' description']
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','address','message']   
    