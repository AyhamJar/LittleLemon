from rest_framework import serializers
from .models import Menu  # Ensure you import the correct model

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'  # This includes all fields from the Menu model
        # Alternatively, you can specify particular fields like this:
        # fields = ['id', 'name', 'price', 'description']
