from django.db import models
from django.contrib.auth.models import User

class SongList(models.Model):
    """
    A user's list of songs
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class SongRating(models.Model):
    """
    How a user has rated a song in their list
    """
    rating_choices = [
        ('1', 'Appalling'),
        ('2', 'Horrible'),
        ('3', 'Very Bad'),
        ('4', 'Bad'),
        ('5', 'Average'),
        ('6', 'Fine'),
        ('7', 'Good'),
        ('8', 'Very Good'),
        ('9', 'Great'),
        ('10', 'Masterpiece'),
    ]

    song = models.ForeignKey('home.Song', on_delete=models.CASCADE)
    parent_list = models.ForeignKey(SongList, on_delete=models.CASCADE)
    rating = models.CharField(max_length=2, choices=rating_choices, default='5')
