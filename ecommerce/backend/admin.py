from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat_name']


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['cat_id', 'title', 'slug', 'image', 'price', 'description']
    search_fields = ('title', 'slug')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['content_img', 'title', 'description', 'bg_image']
    search_fields = ('title', 'content_img')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'mem_image', 'position', 'details']
    search_fields = ('name', 'position')


@admin.register(Storesetting)
class StoresettingAdmin(admin.ModelAdmin):
    list_display = ['s_name', 's_email', 's_phone', 's_logo']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['fname', 'email', 'subject', 'message']
