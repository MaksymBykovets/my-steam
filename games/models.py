from django.db import models
from django.contrib.auth.models import User

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
    
class LibraryItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'game')
        ordering = ['-added_at']

    def __str__(self):
        return f'{self.user.username} - {self.game.title}'