from rest_framework import serializers
from django.contrib.auth.models import User

def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('error email')
    

class UserRegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only=True , required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password' : {'write_only' : True},
            'email' : {'validators' : (clean_email,)},
        }

    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)    


    def validate_username(self, value):
        if value == 'admin':
            raise serializers.ValidationError('user cant be admin')
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('password must match')
        return data