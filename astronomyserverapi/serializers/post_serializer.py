from rest_framework import serializers
from astronomyserverapi.models import Post, PostLikes, PostComments

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        depth = 2


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class PostLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLikes
        fields = "__all__"
        depth = 1

class PostCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = "__all__"
        depth = 1

class CreatePostCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = "__all__"