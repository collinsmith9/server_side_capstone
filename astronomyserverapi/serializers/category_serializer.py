from rest_framework import serializers
from astronomyserverapi.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category')
        depth = 1

