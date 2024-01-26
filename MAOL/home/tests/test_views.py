from django.contrib.auth.models import User
from django.test import TestCase

from home.models import Anime, Song
from personal_list.models import SongRating


class IndexTestCase(TestCase):
    
    def test_get(self):
        res = self.client.get('/')

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home/index.html')


class AnimeListingTestCase(TestCase):
    def test_get(self):
        Anime.objects.create(
            japanese_name='different japanese name',
            english_name='test anime',
            slug_name='test_anime',
            studio='abc-studios',
            anilist_link='https://anilist.co/anime/1',
        )
        Anime.objects.create(
            japanese_name='mushoku tensei',
            english_name='jobless reincarnation',
            slug_name='mushoku_tensei',
            studio='abc-studios',
            anilist_link='https://anilist.co/anime/1',
        )

        res = self.client.get('/anime/')
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home/anime_listing.html')
        self.assertContains(res, 'test anime')
        self.assertContains(res, 'jobless reincarnation')


class AnimeTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.anime = Anime.objects.create(
            japanese_name='mushoku tensei',
            english_name='jobless reincarnation',
            slug_name='mushoku_tensei',
            studio='abc-studios',
            anilist_link='https://anilist.co/anime/1',
        )
        Song.objects.create(
            anime=cls.anime,
            song_type='op',
            number=1,
            name='song name',
            artist='artist name',
        )
    
    def test_get_id_valid(self):
        res = self.client.get(f'/anime/{self.anime.pk}')

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home/anime.html')
        self.assertContains(res, 'jobless reincarnation')
        self.assertContains(res, 'song name')
    
    def test_get_id_invalid(self):
        res = self.client.get('/anime/1999')

        self.assertEqual(res.status_code, 404)


class SongTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        anime = Anime.objects.create(
            japanese_name='mushoku tensei',
            english_name='jobless reincarnation',
            slug_name='mushoku_tensei',
            studio='abc-studios',
            anilist_link='https://anilist.co/anime/1',
        )
        cls.song = Song.objects.create(
            anime=anime,
            song_type='op',
            number=1,
            name='song name',
            artist='artist name',
        )
    
    def test_slug_valid(self):
        res = self.client.get('/song/mushoku_tensei-op-1')

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home/song.html')
        self.assertContains(res, 'song name')
    
    def test_slug_notexist(self):
        """
        When a correctly formatted slug is given, but the song does not exist
        """
        res = self.client.get('/song/mushoku_tensei-op-55')

        self.assertEqual(res.status_code, 404)
    
    def test_slug_invalid(self):
        """
        When an incorrectly formatted slug is given
        """
        res = self.client.get('/song/abc')

        self.assertEqual(res.status_code, 404)


class RandomSongTestCase(TestCase):
    def test_get(self):
        anime = Anime.objects.create(
            japanese_name='mushoku tensei',
            english_name='jobless reincarnation',
            slug_name='mushoku_tensei',
            studio='abc-studios',
            anilist_link='https://anilist.co/anime/1',
        )
        Song.objects.create(
            anime=anime,
            song_type='op',
            number=1,
            name='song name',
            artist='artist name',
        )
        Song.objects.create(
            anime=anime,
            song_type='op',
            number=2,
            name='different song',
            artist='my favourite artist',
        )

        res = self.client.get('/random/')

        self.assertEqual(res.status_code, 302)
        self.assertTrue(res.url.startswith('/song/'))


class TopSongsTestCase(TestCase):
    def test_get(self):
        user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpass')

        anime = Anime.objects.create(
            japanese_name='mushoku tensei',
            english_name='jobless reincarnation',
            slug_name='mushoku_tensei',
            studio='abc-studios',
            anilist_link='https://anilist.co/anime/1',
        )
        song_one = Song.objects.create(
            anime=anime,
            song_type='op',
            number=1,
            name='song name',
            artist='artist name',
        )
        song_two = Song.objects.create(
            anime=anime,
            song_type='op',
            number=2,
            name='different song',
            artist='my favourite artist',
        )
        rating_one = SongRating.objects.create(
            parent_list=user.songlist,
            song=song_one,
            rating=9,
        )
        rating_one = SongRating.objects.create(
            parent_list=user.songlist,
            song=song_two,
            rating=8,
        )

        res = self.client.get('/top/')

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home/top_songs.html')
        self.assertContains(res, 'song name')
        self.assertContains(res, 'different song')


class SearchTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        anime = Anime.objects.create(
            japanese_name='mushoku tensei',
            english_name='jobless reincarnation',
            slug_name='mushoku_tensei',
            studio='abc-studios',
            anilist_link='https://anilist.co/anime/1',
        )
        Song.objects.create(
            anime=anime,
            song_type='op',
            number=1,
            name='song name',
            artist='artist name',
        )
    
    def test_search_query(self):
        res = self.client.get('/search/?q=jobless')

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home/search.html')
        self.assertContains(res, 'jobless reincarnation')
        self.assertContains(res, 'song name')
    
    def test_search_no_query(self):
        res = self.client.get('/search/')

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'No Search Entered')