from rest_framework import serializers
from astronomyserverapi.models import Event, EventLikes, EventComments, EventType

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        depth = 1

class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class EventLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLikes
        fields = "__all__"
        depth = 1

class EventCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventComments
        fields = "__all__"
        depth = 1

class CreateEventCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventComments
        fields = "__all__"

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = "__all__"