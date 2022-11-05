from django.db import models
from django.db.models import Q
from django.utils import timezone


class DateData(models.Model):
    """
    Adds a date_created and last_modified date
    """

    date_created = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.last_modified = timezone.now()
        super().save(*args, **kwargs)


class ModelAbstract(DateData):
    """
    A generic class for models to inherit from,
    adds some nifty universal stuff
    """

    class Meta:
        abstract = True


class AnimeManager(models.Manager):
    def search(self, query):
        qs = self.get_queryset()
        lookup = (
            Q(japanese_name__icontains=query) |
            Q(english_name__icontains=query)
        )

        qs = qs.filter(lookup).distinct()
        return qs


class Anime(ModelAbstract):
    """
    An anime series
    """
    japanese_name = models.TextField()
    english_name = models.TextField()
    slug_name = models.TextField()
    studio = models.TextField()
    anilist_link = models.TextField()
    # cover photo
    cover = models.TextField(default='')

    objects = AnimeManager()

    def __str__(self):
        return self.english_name


class SongManager(models.Manager):
    def get_top_songs(self):
        """
        Get the top rated songs in the database.

        If using this for a carousel, perform
        .values('video_link', 'anime__cover', 'pk')
        on the queryset.

        @limit: How many songs to get
        """

        # Grab the top n songs with the highest ratings
        rated = Song.objects.annotate(
                avg_rating=models.Avg('songrating__rating')
            ).exclude(avg_rating=0).order_by(
                '-avg_rating', 'anime__english_name'
            )
        return rated

    def search(self, query):
        qs = self.get_queryset()
        lookup = (
            Q(name__icontains=query) |
            Q(artist__icontains=query) |
            Q(anime__japanese_name__icontains=query) |
            Q(anime__english_name__icontains=query)
        )

        qs = qs.filter(lookup).distinct().order_by(
            'anime__english_name',
            '-song_type',
            'number'
        )
        return qs


class Song(ModelAbstract):
    """
    An anime track, can be OP, ED, OST.
    """

    objects = SongManager()

    song_type_choices = [
        ('OP', 'Opening'),
        ('ED', 'Ending'),
        ('OST', 'Soundtrack'),
    ]

    song_type = models.CharField(max_length=10, choices=song_type_choices)
    name = models.TextField(default='')
    artist = models.TextField(default='')
    detail_link = models.TextField(default='')
    video_link = models.TextField(default='')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    # E.G OP 1
    number = models.TextField()

    belongs_to_lists = models.ManyToManyField(
        'personal_list.SongList',
        through="personal_list.SongRating"
    )

    def __str__(self):
        """
        Get the name of the Song in regards to the Anime
        e.g Demon Slayer OP 1
        """

        return self.anime.english_name + ' ' + self.song_type + self.number

    def get_song_name(self):
        """
        Get the name of the Song in regards to the real song
        e.g Lisa - Gurenge
        """
        return self.artist + ' ' + self.name
