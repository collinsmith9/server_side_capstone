from socketserver import ThreadingUDPServer
from wsgiref.util import setup_testing_defaults
from django.forms import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from astronomyserverapi.models import EventLikes, Event, siteUser
from astronomyserverapi.serializers import PostLikesSerializer
from astronomyserverapi.serializers.event_serializer import EventLikesSerializer


class EventLikesView(ViewSet):
    def list(self, request):
        event_likes = EventLikes.objects.all()
        user = request.query_params.get("user", None)
        if user is not None:
            event_likes = event_likes.filter(user_id=user)
        serializer = EventLikesSerializer(event_likes, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            event = Event.objects.get(pk=request.data['event'])
            user = siteUser.objects.get(pk=request.data['user'])

            event_like = EventLikes.objects.create(
                event=event,
                user=user
            )
            serializer = EventLikesSerializer(event_like)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Event.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        event_like = EventLikes.objects.get(pk=pk)
        event_like.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

