from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from home.models import ModelAbstract, Song


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
        processors=[ResizeToFill(1300, 400)],
        format="PNG"
    )

    # def get_recent_ratings(self, limit=20):
    #     """
    #     Get the user's recently rated songs.

    #     @limit: How many songs to get
    #     """

    #     ratings = self.user.songlist.songrating_set.all()
    #     songs = Song.objects.filter(songrating__in=ratings).values('video_link', 'anime__cover', 'pk').order_by(
    #         '-songrating__last_modified')[:limit]

    #     return songs

    def get_top_ratings(self, limit=20):
        """
        Get the user's recently rated songs.

        @limit: How many songs to get
        """

        # Grab all the user's ratings
        ratings = self.user.songlist.songrating_set.all()

        # Filter through the highest rated, and then most recently rated songs rated by the user.
        songs = Song.objects.filter(songrating__in=ratings).values('video_link', 'anime__cover', 'pk').order_by(
            '-songrating__rating', 'songrating__last_modified')[:limit]

        return songs

    def __str__(self):
        return self.user.username + '\'s Profile'

# On User creation, make a profile as well
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)


class SongList(ModelAbstract):
    """
    A user's list of songs
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + '\'s List'

# On User creation, make a SongList as well
def create_songlist(sender, instance, created, **kwargs):
    if created:
        SongList.objects.create(user=instance)

    post_save.connect(create_songlist, sender=User)

class SongRating(ModelAbstract):
    """
    How a user has rated a song in their list
    """

    song = models.ForeignKey('home.Song', on_delete=models.CASCADE)
    parent_list = models.ForeignKey(SongList, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(null=True, blank=True, validators=[MaxValueValidator(10)])

    def __str__(self):
        return str(self.rating) + ' ' + str(self.song) 
