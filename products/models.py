from django.db import models
from django.contrib import admin

class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    weight = models.IntegerField()
    height = models.IntegerField()
    color = models.CharField(max_length=7)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Product, ProductAdmin)