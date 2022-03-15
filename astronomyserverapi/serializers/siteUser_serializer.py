from rest_framework import serializers
from astronomyserverapi.models import siteUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = siteUser
        fields = "__all__"
        depth = 2