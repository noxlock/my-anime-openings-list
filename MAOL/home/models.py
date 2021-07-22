from django.db import models

from personal_list.models import SongRating


class Anime(models.Model):
    """
    An anime series
    """
    japanese_name = models.TextField()
    english_name = models.TextField()
    studio = models.TextField()
    anilist_link = models.TextField(default='')

    def __str__(self):
        return self.english_name


class Song(models.Model):
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
    belongs_to_lists = models.ManyToManyField('personal_list.SongList', through=SongRating)

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

    def get_embed_link(self):
        """
        Get an embed friendly link for the song
        (normal '/watch?' doesn't work)
        """

        return self.video_link.replace('watch?v=', 'embed/')
