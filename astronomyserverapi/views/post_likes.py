from socketserver import ThreadingUDPServer
from wsgiref.util import setup_testing_defaults
from django.forms import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from astronomyserverapi.models import PostLikes
from astronomyserverapi.serializers import PostLikesSerializer


class PostLikesView(ViewSet):
    def list(self, request):
        post_likes = PostLikes.objects.all()
        serializer = PostLikesSerializer(post_likes, many=True)
        return Response(serializer.data)