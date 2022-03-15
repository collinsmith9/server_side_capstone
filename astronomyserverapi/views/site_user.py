from socketserver import ThreadingUDPServer
from wsgiref.util import setup_testing_defaults
from django.forms import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from astronomyserverapi.models import siteUser
from django.db.models import Q
from datetime import datetime
from django.contrib.auth.models import User
from astronomyserverapi.serializers import UserSerializer


class UserView(ViewSet):
    def retrieve(self, request, pk):
        try:
            User = siteUser.objects.get(pk=pk)
            serializer = UserSerializer(User)
            return Response(serializer.data)
        except siteUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        user = siteUser.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
