
        
  
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profiles

# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ['bio', 'location', 'birthdate']

# User Serializer with nested Profile Serializer
class UserSerializer(serializers.ModelSerializer):
    profiles = ProfileSerializer()  # Nested Profile Serializer

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profiles']  # Including password and profile fields
        extra_kwargs = {'password': {'write_only': True}}  # Make password write-only

    def create(self, validated_data):
        # Extract the profile data
        profile_data = validated_data.pop('profiles')
        print(profile_data, 'profile_data')
        # Create the user instance
        user = User.objects.create_user(**validated_data)  # Use create_user to handle password hashing
        print(user, 'user')
        # Create the profile instance
        Profiles.objects.create(user=user, **profile_data)
        return user
        
        
     
        
           
