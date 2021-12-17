from django.contrib import auth
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from .models import UserProfile


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=8)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'profession']
        read_only_fields = ['created_at', 'updated_at']
        ordering = ['id']

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=50, min_length=8, write_only=True)
    username = serializers.CharField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'username',)

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials,try again')
        return {
            'email': user.email,
            'username': user.username
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'image', 'first_name', 'last_name', 'about', 'birthday', 'gender']
        read_only_fields = ['owner']
