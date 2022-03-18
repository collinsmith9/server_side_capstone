from socketserver import ThreadingUDPServer
from wsgiref.util import setup_testing_defaults
from django.forms import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from astronomyserverapi.models import PostComments
from astronomyserverapi.serializers import PostCommentsSerializer, CreatePostCommentsSerializer

class PostCommentsView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            comment = PostComments.objects.get(pk=pk)
            serializer = PostCommentsSerializer(comment)
            return Response(serializer.data)
        except PostComments.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        post_comments = PostComments.objects.all()
        post = request.query_params.get("post", None)
        if post is not None:
            post_comments = post_comments.filter(post_id=post)
        serializer = PostCommentsSerializer(post_comments, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk):
        comment = PostComments.objects.get(pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        serializer = CreatePostCommentsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        