from rest_framework import serializers
from .models import Incident
from .models import UserProfile, Report, Assignment
from django.contrib.auth.models import User

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = "__all__"


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}



class UserSerializer(serializers.ModelSerializer):
    # extra field for role (coming from UserProfile)
    role = serializers.ChoiceField(choices=UserProfile.ROLE_CHOICES, write_only=True)
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "role"]

    def create(self, validated_data):
        role = validated_data.pop("role")  # take out role before creating user
        password = validated_data.pop("password")

        # create user
        user = User(**validated_data)
        user.set_password(password)  # hash password
        user.save()

        # create linked UserProfile
        UserProfile.objects.create(user=user, role=role)

        return user

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    password = serializers.CharField(write_only=True, source="user.password")
    email = serializers.EmailField(source="user.email")

    class Meta:
        model = UserProfile
        fields = ["id", "username", "password", "email", "role"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create_user(
            username=user_data["username"],
            email=user_data["email"],
            password=user_data["password"]
        )
        profile = UserProfile.objects.create(user=user, **validated_data)
        return profile



class ReportSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Report
        fields = ["id", "title", "description", "created_by", "created_at"]


class AssignmentSerializer(serializers.ModelSerializer):
    report = ReportSerializer(read_only=True)
    volunteer = UserProfileSerializer(read_only=True)

    class Meta:
        model = Assignment
        fields = ["id", "report", "volunteer", "status", "assigned_at"]



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # remove password2
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims (extra info in token)
        token['username'] = user.username
        token['email'] = user.email

        # If you want to include related profile fields (optional):
        if hasattr(user, 'userprofile'):
            token['location'] = user.userprofile.location
            token['phone_number'] = user.userprofile.phone_number

        return token
