from django.forms import ModelForm, MultipleChoiceField
from .models import Pizza
from django import forms


class CustomerForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ('pizza_type', 'pizza_size', 'onion', 'tomato', 'corn', 'capsicum', 'cheese', 'jalapeno')
