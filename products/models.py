from django.db import models
from django.contrib import admin
#from django.forms import ModelForm, CharField, Textarea
from django import forms

class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    weight = models.IntegerField()
    height = models.IntegerField()
    color = models.CharField(max_length=7, verbose_name='Color 1')
    colortwo = models.CharField(max_length=7, default='#000', verbose_name='Color 1')
    image = models.ImageField(upload_to='images', blank=True, default='images/default.jpg')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=30,label='')
    weight = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}))
    height = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}))
    color = forms.CharField(widget=forms.TextInput(attrs={'class':'cpinput1 input-small'}))
    colortwo = forms.CharField(widget=forms.TextInput(attrs={'class':'cpinput2 input-small'}))
    image = forms.FileInput()
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)