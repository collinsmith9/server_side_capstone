from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from astronomyserverapi.models import Follow
from astronomyserverapi.models import siteUser
from astronomyserverapi.serializers import FollowSerializer

class FollowView(ViewSet):
    def retrieve(self, request, pk):
        follow = Follow.objects.get(pk=pk)
        serializer = FollowSerializer(follow)
        return Response(serializer.data)

    def list(self, request):
        follows = Follow.objects.all()
        person_followed = request.query_params.get('personfollowed', None)
        if person_followed is not None:
            follows = follows.filter(person_followed=person_followed)
        serializer = FollowSerializer(follows, many=True)
        return Response(serializer.data)

    def create(self, request):
        follower = siteUser.objects.get(pk=request.data['follower'])
        person_followed = siteUser.objects.get(pk=request.data["person_followed"])

        follow = Follow.objects.create(
            follower=follower,
            person_followed=person_followed
        )
        serializer = FollowSerializer(follow)
        return Response(serializer.data)

    def destroy(self, request, pk):
        follow = Follow.objects.get(pk=pk)
        follow.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)