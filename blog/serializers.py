from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Blogpost

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        fields = ['id', 'title', 'content', 'author', 'pub_date']
