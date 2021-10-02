from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from home.models import ModelAbstract


class Profile(ModelAbstract):
    """
    A user's profile. Data like profile picture/banner is stored here,
    but also anything else that should probably be extending the
    default User model.
    
    It takes hard work to set a custom User model once you've already
    started a project, and most of the things I want would
    fit nicely in a model like this anyways.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = ProcessedImageField(
        upload_to='avatars', default='avatars/placeholder.png',
        processors=[ResizeToFill(256, 256)],
        format="PNG"
    )
    banner = ProcessedImageField(
        upload_to='banners', default='banners/placeholder.png',
        processors=[ResizeToFill(256, 256)],
        format="PNG"
    )

    def get_recent_ratings(self):
        pass

    def get_top_ratings(self):
        pass

    def __str__(self):
        return self.user.username + '\'s Profile'

# On User creation, make a profile as well
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


class SongList(ModelAbstract):
    """
    A user's list of songs
    """

    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.username + '\'s List'

class SongRating(ModelAbstract):
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
    rating = models.CharField(max_length=2, choices=rating_choices, null=True, blank=True)

    def __str__(self):
        return self.rating
