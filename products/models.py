from django.db import models
from django.contrib import admin
from django.core import mail
from django import forms
from django.db.models.signals import pre_save, pre_delete, post_save
from django.dispatch import receiver

class Resp(models.Model):
    url = models.CharField(max_length=200)
    method = models.CharField(max_length=10)
    status_code = models.IntegerField()

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

def mailsender(msg, product_title):
    connection = mail.get_connection()
    connection.open()
    email1 = mail.EmailMessage('Hello', 'Product "'+product_title+'" '+msg, 'from@example.com',
                      ['to1@example.com'], connection=connection)
    email1.send()
    connection.close()

@receiver(pre_delete, sender=Product)
def pre_del(sender, instance, **kwargs):
    mailsender('deleted', instance.title)

@receiver(post_save, sender=Product)
def post_sv(sender,instance, signal, created, **kwargs):
    if created:
        mailsender('created', instance.title)
    else:
        mailsender('edited', instance.title)

admin.site.register(Product, ProductAdmin)
admin.site.register(Resp)
