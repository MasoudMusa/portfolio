from django.db import models

# Create your models here.
from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True) 

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')
    tech_stack = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    description = models.TextField()
    
    def __str__(self):
        return self.title
