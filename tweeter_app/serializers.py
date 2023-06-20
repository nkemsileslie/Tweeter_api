from rest_framework import serializers
from .models import Profile, Tweet, Comment

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profilefields = '__all__'

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
