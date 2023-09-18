from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=127,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='email already registered.'
            )]
        )
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(required=False)
    is_employee = serializers.BooleanField(required=False)
    username = serializers.CharField(
        max_length=150,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='username already taken.'
            )]
        )
    password = serializers.CharField(max_length=128, write_only=True)
    id = serializers.IntegerField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict) -> User:
        if validated_data.get('is_employee'):
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            elif attr in ('is_superuser', 'is_employee'):
                pass
            else:
                setattr(instance, attr, value)

        instance.save()

        return instance
