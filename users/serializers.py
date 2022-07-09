from rest_framework import serializers
from .models import Employee

# User Serializer


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'username', 'email', 'company', 'shift')

# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'username', 'email', 'password', 'company', 'shift')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Employee.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'], validated_data['company'], validated_data['shift'])

        return user


class ChangePasswordSerializer(serializers.Serializer):

    model = Employee
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
