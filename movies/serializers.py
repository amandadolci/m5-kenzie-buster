from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Movie, MovieOrder


RATING_CHOICES = ('G', 'PG', 'PG-13', 'R', 'NC-17')

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(
        max_length=127,
        validators=[UniqueValidator(
            queryset=Movie.objects.all(),
            message='movie already registered.'
            )]
        )
    duration = serializers.CharField(max_length=10, required=False)
    rating = serializers.ChoiceField(
        choices=RATING_CHOICES,
        required=False
        )
    synopsis = serializers.CharField(required=False)
    id = serializers.IntegerField(read_only=True)
    added_by = serializers.EmailField(read_only=True, source='user.email')

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True, source='movie.title')
    bought_by = serializers.EmailField(read_only=True, source='user.email')
    bought_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)