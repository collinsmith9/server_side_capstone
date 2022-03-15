from rest_framework import serializers, status
from astronomyserverapi.models import Follow

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'
        depth = 1