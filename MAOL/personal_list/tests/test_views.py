import json

from django.contrib.auth.models import User
from django.test import TestCase

from home.models import Anime, Song
from personal_list.models import SongRating, Profile, SongList


class ProfileViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Django signals should automatically create a Profile and Songlist
        cls.user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpass')
    
    def test_profile_id_exists(self):
        """
        Make sure that a profile page is returned when an existing profile is passed in.
        """

        res = self.client.get('/profile/testuser/')

        self.assertEqual(res.status_code, 200)
    
    def test_profile_id_doesnt_exist(self):
        """
        Make sure that a 404 page is returned when a profile doesn't exist.
        """

        res = self.client.get('/profile/abc/')

        self.assertEqual(res.status_code, 404)
    
    def test_profile_no_id_authenticated(self):
        """
        When a user is logged in, and no id is passed in, make sure that the
        user is redirected to their own profile.
        """
        self.client.login(username='testuser', password='testpass')

        res = self.client.get('/profile/')
        self.assertRedirects(res, '/profile/testuser/')
    
    def test_profile_no_id_unauthenticated(self):
        """
        When a user is NOT logged in, and no id is passed in, make sure that the
        user is redirected to the login page
        """

        res = self.client.get('/profile/')
        self.assertRedirects(res, '/auth/login/?next=/profile/')


class ListTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpass')
        anime = Anime.objects.create(
            japanese_name="different japanese name",
            english_name="test anime",
            slug_name="test_anime",
            studio="abc studios",
            anilist_link="https://anilist.co/anime/1",
        )
        song = Song.objects.create(
            song_type="OP",
            name="test song",
            artist="test artist",
            anime=anime,
            number="1",
        )
        SongRating.objects.create(
            parent_list=cls.user.songlist,
            song=song,
            rating=5
        )
    
    def test_get_id_valid(self):
        res = self.client.get('/profile/testuser/list/')

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'test song')

    def test_get_id_invalid(self):
        res = self.client.get('/profile/abc/list/')

        self.assertEqual(res.status_code, 404)