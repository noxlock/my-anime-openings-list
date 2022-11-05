from django.db import models
from django.db.models.signals import post_save
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

    def get_top_ratings(self, limit=20):
        """
        Get the user's recently rated songs.

        Gets very little details, mainly just used for carousels.

        @limit: How many songs to get (default 20)
        """

        # Grab all the user's ratings
        ratings = self.user.songlist.songrating_set.all()

        # Filter through the highest rated, and then
        # most recently rated songs rated by the user.
        songs = Song.objects.filter(
            songrating__in=ratings
        ).values(
            'pk',
            'video_link',
            'anime__cover'
        ).order_by('-songrating__rating', 'songrating__last_modified')[:limit]

        return songs

    def get_rated_songs(self, limit=None):
        """
        Grab all songs that a User has rated.
        Used for the user's list.

        @limit: How many songs to get
        """

        # Grab all the user's SongRatings, along with details about the song.
        ratings = SongRating.objects.filter(
            parent_list=self.user.songlist
        ).values(
            'song__anime__cover',
            'song__anime__english_name',
            'song__anime__slug_name',
            'song__anime__pk',
            'song__song_type',
            'song__number',
            'song__name',
            'rating',
            'song__video_link',
            'song__detail_link',
            'song__pk'
        ).order_by(
            '-rating',
            'song__anime__english_name',
            '-song__song_type', 'song__number'
        )

        return ratings

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


# On User creation, make a profile as well
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
    rating = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(10)]
        )

    class Meta:
        # You should only be able to have one rating per song.
        constraints = [
            models.UniqueConstraint(
                fields=['parent_list', 'song'],
                name='one_rating_only'
            )
        ]

    def __str__(self):
        return str(self.rating) + ' ' + str(self.song)
