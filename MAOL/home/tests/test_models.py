from django.contrib.auth.models import User
from django.test import TestCase

from home.models import Anime, Song
from personal_list.models import SongRating


class AnimeManagerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        anime = Anime(
            japanese_name='different japanese name',
            english_name='test anime',
            studio='abc-studios',
            slug_name='test_anime',
            anilist_link='https://www.test.com'
        )
        anime.save()

    def test_search_english(self):
        
        qs = Anime.objects.search('test')

        self.assertEqual('test anime', qs[0].english_name)
    
    def test_search_japanese(self):
        
        qs = Anime.objects.search('japanese')

        self.assertEqual('different japanese name', qs[0].japanese_name)
    
    def test_search_not_exist(self):
            
        qs = Anime.objects.search('something that doesn\'t exist')

        self.assertEqual(0, len(qs))


class AnimeTestCase(TestCase):
    def test_str(self):
        anime = Anime(
            japanese_name='tesuto',
            english_name='test anime',
            studio='abc-studios',
            slug_name='test_anime',
            anilist_link='https://www.test.com'
        )
        anime.save()

        self.assertEqual(str(anime), 'test anime')


class SongManagerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpass')

        anime = Anime.objects.create(
            japanese_name='different japanese name',
            english_name='test anime',
            studio='abc-studios',
            slug_name='test_anime',
            anilist_link='https://www.test.com'
        )

        song_one = Song.objects.create(
            song_type='ED',
            name='Wind',
            artist='Akeboshi',
            anime=anime,
            number='1',
        )

        song_two = Song.objects.create(
            song_type='OP',
            name='Haruka Kanata',
            artist='ASIAN KUNG-FU GENERATION',
            anime=anime,
            number='2',
        )

        song_three = Song.objects.create(
            song_type='OP',
            name='Inferno',
            artist='Mrs. Green Apple',
            anime=anime,
            number='3',
        )

        # Make sure songs with no ratings aren't included in
        # get_top_songs
        song_four = Song.objects.create(
            song_type='OP',
            name='Size of the moon',
            artist='Akeboshi',
            anime=anime,
            number='14',
        )

        rating_one = SongRating.objects.create(
            parent_list=user.songlist,
            song=song_one,
            rating=10
        )

        rating_two = SongRating.objects.create(
            parent_list=user.songlist,
            song=song_two,
            rating=5
        )

        rating_three = SongRating.objects.create(
            parent_list=user.songlist,
            song=song_three,
            rating=9
        )
    
    def test_get_top_songs(self):
        top_songs = Song.objects.get_top_songs()

        self.assertEqual('Wind', top_songs[0].name)
        self.assertEqual('Inferno', top_songs[1].name)
        self.assertEqual('Haruka Kanata', top_songs[2].name)
        self.assertEqual(3, len(top_songs))
    
    def test_get_top_songs_limit(self):
        top_songs = Song.objects.get_top_songs(1)

        self.assertEqual('Wind', top_songs[0].name)
        self.assertEqual(1, len(top_songs))
    
    def test_search_song_name(self):
            
        qs = Song.objects.search('wind')

        self.assertEqual('Wind', qs[0].name)
    
    def test_search_artist_name(self):
                
        qs = Song.objects.search('akeboshi')

        self.assertEqual('Akeboshi', qs[0].artist)
        self.assertEqual(2, len(qs))

    def test_search_anime_english_name(self):
        
        qs = Song.objects.search('test')

        self.assertEqual('test anime', qs[0].anime.english_name)

        # Since all the songs are from the same anime, we should have four songs.
        self.assertEqual(4, len(qs))
    
    def test_search_anime_japanese_name(self):
        
        qs = Song.objects.search('japanese')

        self.assertEqual('different japanese name', qs[0].anime.japanese_name)
        self.assertEqual(4, len(qs))
    
    def test_search_not_exist(self):
            
        qs = Song.objects.search('something that doesn\'t exist')

        self.assertEqual(0, len(qs))


class SongTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        anime = Anime(
            japanese_name='different japanese name',
            english_name='test anime',
            studio='abc-studios',
            slug_name='test_anime',
            anilist_link='https://www.test.com'
        )

        cls.song = Song(
            song_type='ED',
            name='Wind',
            artist='Akeboshi',
            anime=anime,
            number='1',
        )

    def test_str(self):
        self.assertEqual(str(self.song), 'test anime ED1')
    
    def test_get_song_name(self):
        self.assertEqual('Akeboshi Wind', self.song.get_song_name())
