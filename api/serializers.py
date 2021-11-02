from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api.models import Profile, Resume


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProfileSerializer(serializers.ModelSerializer):

    resume = serializers.HyperlinkedRelatedField(many=True, view_name='resume-detail', queryset=Resume.objects.all())

    class Meta:
        model = Profile
        fields = ['active', 'name', 'resume']

class ResumeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resume
        fields = ['name', 'file', 'profile']