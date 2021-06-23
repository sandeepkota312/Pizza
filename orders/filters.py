from .models import Pizza
import django_filters


class pizzaFilter(django_filters.FilterSet):
    class Meta:
        model = Pizza
        fields = ['pizza_type', 'pizza_size', ]
