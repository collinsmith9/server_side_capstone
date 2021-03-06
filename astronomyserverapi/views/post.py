from socketserver import ThreadingUDPServer
from wsgiref.util import setup_testing_defaults
from django.forms import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.db.models import Q
from datetime import datetime
from astronomyserverapi.models.category import Category
from astronomyserverapi.serializers import PostSerializer, CreatePostSerializer
from astronomyserverapi.models import Post
from django.core.files.base import ContentFile
import base64
import uuid
from astronomyserverapi.models import siteUser




class PostView(ViewSet):
    def retrieve(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        posts = Post.objects.all()
        user = request.query_params.get("user", None)
        if user is not None:
            posts = posts.filter(user_id=user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            theuser = siteUser.objects.get(pk=request.data["user"])
            format, imgstr = request.data["post_pic"].split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["user"]}-{uuid.uuid4()}.{ext}')
            post = Post.objects.create(
                user = theuser,
                caption = request.data["caption"],
                post_pic = data
            )
            post.categories.set(request.data["categories"])
            return Response(None, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        post = Post.objects.get(pk=pk)
        theuser = siteUser.objects.get(pk=request.data["user"])
        if ';base64,' in request.data["post_pic"]:
            format, imgstr = request.data["post_pic"].split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["user"]}-{uuid.uuid4()}.{ext}')
            updated_post = {
                'user': request.data["user"],
                'caption': request.data["caption"]
            }
            
            serializer = CreatePostSerializer(post, updated_post)
            serializer.is_valid(raise_exception=True)
            post = serializer.save(post_pic=data)
            
            post.categories.set(request.data["categories"])
        else:

            updated_post = {
                    'user': request.data["user"],
                    'caption': request.data["caption"]
                }
                
            serializer = CreatePostSerializer(post, updated_post)
            serializer.is_valid(raise_exception=True)
            post = serializer.save()
                
            post.categories.set(request.data["categories"])
        
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)

        


