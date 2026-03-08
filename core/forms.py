from django import forms
from .models import LostItem, FoundItem


class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = ['item_name', 'category', 'contact', 'location_lost', 'description', 'image', 'date_lost']

        widgets = {
            'item_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. Black Wallet'
            }),
            'category': forms.Select(attrs={
                'class': 'form-input'
            }),
            
            'contact' : forms.TextInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Preferably Phone Number',
            }),

            'location_lost': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. Library, Lecture Hall'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Add more details about the item'
            }),
            'date_lost' : forms.DateInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'yyyy-mm-dd',
            })

            
        }


class FoundItemForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        fields = ['item_name', 'category', 'contact', 'location_found', 'description', 'date_found', 'image']

        widgets = {
            'item_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. Student ID Card'
            }),
            'category': forms.Select(attrs={
                'class': 'form-input'
            }),
            'contact' : forms.TextInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Preferably Phone Number',
            }),
            'location_found': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. Cafeteria, Hostel'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Describe where and how it was found'
            }),
            'date_found' : forms.DateInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'yyyy-mm-dd',
            })
            
        }