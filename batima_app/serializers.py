from rest_framework import serializers
from .models import Habitant, Syndic, Residence, Reglement

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

class UserLoginSerializer(serializers.Serializer):
    email_or_username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        email_or_username = data.get('email_or_username')
        password = data.get('password')

        # Check if the input is an email address
        if '@' in email_or_username:
            # Authenticate using email
            user = authenticate(email=email_or_username, password=password)
        else:
            # Authenticate using username
            user = authenticate(username=email_or_username, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email/username or password")

        refresh = RefreshToken.for_user(user)

        # Customize the token with additional claims
        refresh['user_id'] = user.id
        refresh['email'] = user.email

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class HabitantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitant
        fields = '__all__'


class SyndicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syndic
        fields = '__all__'


class ResidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residence
        fields = '__all__'


class ReglementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reglement
        fields = '__all__'