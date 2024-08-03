from django.db import models

# Create your models here.

class Game(models.Model):
    board = models.CharField(max_length=9, default=' ' * 9)  # 9 spaces for 3x3 board
    current_turn = models.CharField(max_length=1, default='X')  # X or O
    winner = models.CharField(max_length=1, null=True, blank=True)  # X, O, or None
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Game {self.id}: {self.board}"

