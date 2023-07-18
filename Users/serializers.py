from rest_framework import serializers
from . models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'username':{'trim_whitespace': True}, 'password':{'trim_whitespace': True}, 'email':{'trim_whitespace': True}}

    def validate_username(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("username must be 8 characters")
        else:
            return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("username must be 8 characters")
        else:
            return value
        