from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 
        # 'first_name', 'last_name',
         'username', 'password', 'role']

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'], 
            username=validated_data['username'],
            # first_name=validated_data['first_name'],
            # last_name = validated_data['last_name'],
            role = validated_data['role']
            )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')
            