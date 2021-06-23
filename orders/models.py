from django.db import models


class Pizza(models.Model):
    class Type(models.TextChoices):
        REGULAR = 'regular',
        SQUARE = 'square',

    class Size(models.TextChoices):
        SMALL = 'small',
        MEDIUM = 'medium',
        LARGE = 'large',

    class Toppings(models.TextChoices):
        Onion = 'onion',
        Tomato = 'tomato',
        Corn = 'corn',
        Capsicum = 'capsicum',
        Cheese = 'cheese',
        Jalapeno = 'jalapeno',

    pizza_type = models.CharField(max_length=10, choices=Type.choices, default=Type.REGULAR, )
    pizza_size = models.CharField(max_length=10, choices=Size.choices, default=Size.MEDIUM, )
    onion = models.BooleanField(default=False)
    tomato = models.BooleanField(default=False)
    corn = models.BooleanField(default=False)
    capsicum = models.BooleanField(default=False)
    cheese = models.BooleanField(default=False)
    jalapeno = models.BooleanField(default=False)

    def __str__(self):
        return self.pizza_type
