from django.contrib.auth.models import User
from django.test import TestCase

from home.models import Anime, Song
from personal_list.models import SongRating


class ProfileTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpass')
        anime = Anime.objects.create(
            japanese_name="different japanese name",
            english_name="test anime",
            studio="abc-studios",
            slug_name="test_anime",
            anilist_link="https://www.test.com",
        )
        song = Song.objects.create(
            anime=anime,
            song_type="OP",
            number="1",
            name="test song",
        )
        rating = SongRating.objects.create(
            parent_list=user.songlist,
            song=song,
            rating=8
        )
        awesome = self.G(Anime, english_name="awesome anime")



class SongListTestCase(TestCase):
    def test_str(self):
        user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpass')
        self.assertEqual(str(user.songlist), 'testuser\'s List')


class SongRatingTestCase(TestCase):
    def test_str(self):
        user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpass')
        anime = Anime.objects.create(
            japanese_name="different japanese name",
            english_name="test anime",
            studio="abc-studios",
            slug_name="test_anime",
            anilist_link="https://www.test.com",
        )
        song = Song.objects.create(
            anime=anime,
            song_type="OP",
            number="1",
            name="test song",
        )
        rating = SongRating.objects.create(
            parent_list=user.songlist,
            song=song,
            rating=8
        )

        self.assertEqual(str(rating), '8 test anime OP1')