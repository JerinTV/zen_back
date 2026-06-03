# users/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User # Django's built-in User model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email') # You can also add 'email' here if you want it required for signup
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': False} # Set to True if email is mandatory for signup
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        # Remove password2 as it's not part of the User model
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

# This is your existing login serializer, include it here if it's not already in users/serializers.py
# If it's elsewhere (e.g., in zentodo_backend/urls.py or views.py), you can move it here for organization.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        # You can add more claims here if needed
        return token