from django import forms
from .models import Contact


class ContactForm(forms.Form):
    first_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),label="Ім'я")
    last_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),label="Прізвище")
    phone_number=forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),label="Номер телефону")
    email=forms.CharField(max_length=20,required=False,widget=forms.EmailInput(attrs={"class":"form-control"}),label="Електронна адреса")
    address=forms.CharField(max_length=20,required=False,widget=forms.TextInput(attrs={"class":"form-control"}),label="Адреса")
    
    class Meta:
        model=Contact
        fields=("first_name","last_name","phone_number","email","address",)