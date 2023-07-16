from rest_framework import serializers
# from django.contrib.auth.models import User
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
        

        
class ChangePasswordSerializer(serializers.Serializer):
        new_password = serializers.CharField(required=True, write_only=True)
        confirm_new_password = serializers.CharField(required=True, write_only=True)
        password = serializers.CharField(required=True, write_only=True)

        class Meta:
            model = User
            fields= ('password','new_password', 'confirm_new_password')

        # def validate(self, data):
        #     if data['new_password'] != data['confirm_new_password']:
        #         raise serializers.ValidationError({"new_password": "Password fields do not match."})
        #     return data
        
        # def validate_old_password(self, data):
        #     user = self.context['request'].user
        #     if not user.check_password(data):
        #         raise serializers.ValidationError({"password": "Old Password is not correct"})
        #     return data
        
        # def update(self, instance, validated_data):
        #     instance.set_password(validated_data['new_password'])
        #     instance.save()

        #     return instance
        
