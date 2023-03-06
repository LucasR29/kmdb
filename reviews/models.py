from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    stars = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="reviews"
    )
    critic = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews"
    )
