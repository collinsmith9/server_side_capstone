from socketserver import ThreadingUDPServer
from wsgiref.util import setup_testing_defaults
from django.forms import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from astronomyserverapi.models import PostLikes, Post, siteUser
from astronomyserverapi.serializers import PostLikesSerializer, CreatePostLikesSerializer


class PostLikesView(ViewSet):
    def list(self, request):
        post_likes = PostLikes.objects.all()
        user = request.query_params.get("user", None)
        if user is not None:
            post_likes = post_likes.filter(user_id=user)
        serializer = PostLikesSerializer(post_likes, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        try:
            post = Post.objects.get(pk=request.data['post'])
            user = siteUser.objects.get(pk=request.data['user'])

            post_like = PostLikes.objects.create(
                post=post,
                user=user
            )
            serializer = PostLikesSerializer(post_like)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        post_like = PostLikes.objects.get(pk=pk)
        post_like.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    