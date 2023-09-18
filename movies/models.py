from django.db import models
from users.models import User


class Rating(models.TextChoices):
    G = 'G'
    PG = 'PG'
    PG_13 = 'PG-13'
    R = 'R'
    NC_17 = 'NC-17'


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        choices=Rating.choices,
        default=Rating.G,
        null=True
        )
    synopsis = models.TextField(null=True, default=None)
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='movies',
    )
    order = models.ManyToManyField(
        User, 
        through="movies.MovieOrder", 
        related_name="movie_order"
)
    
class MovieOrder(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    bought_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
