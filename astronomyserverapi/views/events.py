from socketserver import ThreadingUDPServer
from wsgiref.util import setup_testing_defaults
from django.forms import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.db.models import Q
from datetime import datetime
from astronomyserverapi.models.event_type import EventType
from astronomyserverapi.serializers import EventSerializer, CreateEventSerializer
from astronomyserverapi.models import Event, siteUser
from django.core.files.base import ContentFile
import base64
import uuid



class EventView(ViewSet):
    def retrieve(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            theuser = siteUser.objects.get(pk=request.data["user"])
            event_type = EventType.objects.get(pk=request.data["event_type"])
            format, imgstr = request.data["event_pic"].split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["user"]}-{uuid.uuid4()}.{ext}')
            event = Event.objects.create(
                user = theuser,
                name = request.data["name"],
                description = request.data["description"],
                seen_from = request.data["seen_from"],
                event_type = event_type,
                is_approved = request.data["is_approved"],
                event_pic = data
            )
            return Response(None, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)