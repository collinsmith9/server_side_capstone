from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from astronomyserverapi.models import EventType
from astronomyserverapi.serializers import EventTypeSerializer


class EventTypeView(ViewSet):
    def retrieve(self, request, pk):
        try:
            event_type = EventType.objects.get(pk=pk)
            serializer = EventTypeSerializer(event_type)
            return Response(serializer.data)
        except EventType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        event_types = EventType.objects.all()
        serializer = EventTypeSerializer(event_types, many=True)
        return Response(serializer.data)