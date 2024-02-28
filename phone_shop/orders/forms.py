from cProfile import label
from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        labels = {'first_name':'Имя',
                  'last_name':'Фамилия', 
                  'email':'Почта', 
                  'address':'Адрес', 
                  'postal_code':'Почтовый индекс', 
                  'city':'Город'}
        widgets = {
            "first_name": forms.TextInput(attrs={
                'placeholder': 'Имя',
                'label': 'Имя'
            }),
            "last_name": forms.TextInput(attrs={
                'placeholder': 'Фамилия',
                'label': 'Имя'
            }),
            "email":forms.TextInput(attrs={
                'placeholder': 'Почта',
                'label': 'Имя'
            }),
            "address":forms.TextInput(attrs={
                'placeholder': 'Адрес',
                'label': 'Имя'
            }),
            "postal_code":forms.TextInput(attrs={
                'placeholder': 'Почтовый индекс',
                'label': 'Имя'
            }),
            "city":forms.TextInput(attrs={
                'placeholder': 'Город',
                'label': 'Имя'
            }),
                        
        }