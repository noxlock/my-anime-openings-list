from django.db import models
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
        last_modified = timezone.now()
        super().save(*args, **kwargs)



class ModelAbstract(DateData):
    """
    A generic class for models to inherit from,
    adds some nifty universal stuff
    """

    class Meta:
        abstract = True


class Anime(ModelAbstract):
    """
    An anime series
    """
    japanese_name = models.TextField()
    english_name = models.TextField()
    studio = models.TextField()
    anilist_link = models.TextField()
    # cover photo
    cover = models.TextField(default='')

    def __str__(self):
        return self.english_name


class Song(ModelAbstract):
    """
    An anime track, can be OP, ED, OST.
    """
    song_type_choices = [
        ('OP', 'Opening'),
        ('ED', 'Ending'),
        ('OST', 'Soundtrack'),
    ]

    song_type = models.CharField(max_length=3, choices=song_type_choices)
    name = models.TextField(default='')
    artist = models.TextField(default='')
    video_link = models.TextField(default='')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    # E.G OP 1
    number = models.TextField()
    belongs_to_lists = models.ManyToManyField('personal_list.SongList', through="personal_list.SongRating")

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
