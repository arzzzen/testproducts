from django.db import models
from django.contrib import admin
from django.forms import ModelForm

class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    weight = models.IntegerField()
    height = models.IntegerField()
    color = models.CharField(max_length=7)
    image = models.ImageField(upload_to='images', blank=True, default='images/default.jpg')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ProductForm(ModelForm):
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)