from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    developer = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='game_covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title