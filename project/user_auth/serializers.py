from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User
import re

class RegisterSerializer(serializers.Serializer):
    username = serializers.RegexField(
        regex=r'^[a-zA-Z0-9_]+$',
        required=True,
        error_messages={
            'invalid': 'Username should contain only letters, numbers, and underscores.'
        }
    )
    email = serializers.EmailField(required=True)
    password = serializers.CharField()

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        if 'username' not in validated_data:
            raise ValidationError('Username should be provided')
        if 'email' not in validated_data:
            raise ValidationError('Email should be provided')

        return validated_data
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save(update_fields=['password'])
        return user

        password = validated_data.pop('password',None)
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save(update_fields=['password'])
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField()

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','firstname','lastname')