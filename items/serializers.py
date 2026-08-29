from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    createdAt = serializers.DateTimeField(source='created_at', read_only=True)
    updatedAt = serializers.DateTimeField(source='updated_at', read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'category', 'status', 'priority', 'price', 'createdAt', 'updatedAt']
