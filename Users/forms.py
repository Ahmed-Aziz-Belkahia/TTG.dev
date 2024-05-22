from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    TYPE_CHOICES = [
        ('profit', 'Profit'),
        ('loss', 'Loss'),
    ]

    type = forms.ChoiceField(choices=TYPE_CHOICES)

    class Meta:
        model = Transaction
        fields = ['type', 'pair', 'amount', 'img', 'status']
        widgets = {
            'pair': forms.TextInput(attrs={'placeholder': 'e.g., BTC/USD'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'e.g., 1000'}),
            'img': forms.ClearableFileInput(attrs={'placeholder': 'Upload your proof'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class OrderForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    address = forms.CharField(label="Address", max_length=200)
    city = forms.CharField(label="City", max_length=100)
    state = forms.CharField(label="State", max_length=100)
    zip_code = forms.CharField(label="Zip Code", max_length=10)