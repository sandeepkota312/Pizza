from rest_framework import serializers
from .models import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza  # this is the model that is being serialized
        fields = '__all__'
