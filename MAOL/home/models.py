from django.db import models

from personal_list.models import SongList, SongRating

class Anime(models.Model):
    """
    An anime series
    """
    name = models.TextField()
    studio = models.TextField()
    mal_link = models.TextField(verbose_name='MyAnimeList Link', default='')

    def __str__(self):
        return self.name


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
    name = models.TextField()
    artist = models.TextField()
    video_link = models.TextField(default='')
    embed_link = models.TextField(default='')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    # E.G OP 1
    number = models.TextField()
    belongs_to_lists = models.ManyToManyField('personal_list.SongList', through=SongRating)

    def __str__(self):
        """
        Get the name of the Song in regards to the Anime
        e.g Demon Slayer OP 1
        """

        return self.anime.name + ' ' + self.song_type + self.number
    
    def save(self, *args, **kwargs):
        """
        Make it so we only need to get the youtube video link,
        which is much easier.
        """
        if not self.embed_link:
            self.embed_link = self.get_embed_link()
        
        super().save(*args, **kwargs)

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

