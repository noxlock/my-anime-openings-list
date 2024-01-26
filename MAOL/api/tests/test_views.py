import json

from django.contrib.auth.models import User
from django.test import TestCase

from home.models import Anime, Song
from personal_list.models import SongRating

class ListCRUDTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpass')

        anime = Anime(
            japanese_name='tesuto',
            english_name='test anime',
            studio='abc-studios',
            slug_name='test_anime',
            anilist_link='https://www.test.com'
        )
        anime.save()
        cls.song = Song(anime=anime, song_type='OP', number='1')
        cls.song.save()

    def test_add_to_list_success(self):
        self.client.login(username='testuser', password='testpass')

        res = self.client.post('/api/ratings/', {'song': self.song.pk, 'rating': 5, 'parent_list': self.user.songlist.pk})

        self.assertEqual(res.status_code, 201)
        self.assertTrue(SongRating.objects.filter(song=self.song, rating=5, parent_list=self.user.songlist).exists())

    def test_add_to_list_fail(self):
        self.client.login(username='testuser', password='testpass')

        res = self.client.post('/api/ratings/', {'song': 'abc', 'rating': 5, 'parent_list': self.user.songlist.pk})

        self.assertEqual(res.status_code, 400)

    def test_delete_from_list_success(self):
        self.client.login(username='testuser', password='testpass')

        rating = SongRating(song=self.song, rating=5, parent_list=self.user.songlist)
        rating.save()

        res = self.client.delete(f'/api/ratings/{rating.pk}/')

        self.assertEqual(res.status_code, 204)
        self.assertFalse(SongRating.objects.filter(song=self.song, rating=5, parent_list=self.user.songlist).exists())

    def test_delete_from_list_fail(self):
        self.client.login(username='testuser', password='testpass')

        res = self.client.delete('/api/ratings/500/')

        self.assertEqual(res.status_code, 404)

    def test_edit_rating_success(self):
        self.client.login(username='testuser', password='testpass')

        rating = SongRating(song=self.song, rating=5, parent_list=self.user.songlist)
        rating.save()

        data = json.dumps({'rating': '10'})

        res = self.client.patch(f'/api/ratings/{rating.pk}/', data, content_type='application/json')

        self.assertEqual(res.status_code, 200)
        self.assertTrue(SongRating.objects.filter(song=self.song, rating=10, parent_list=self.user.songlist).exists())
    
    def test_edit_rating_fail(self):
        self.client.login(username='testuser', password='testpass')

        res = self.client.patch(f'/api/ratings/fail/')

        self.assertEqual(res.status_code, 404)