from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from home.models import Anime, Song
from personal_list.models import SongRating

from api.permissions import IsOwner

class IsOwnerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('testuser')
        cls.factory = RequestFactory()

        anime = Anime(
            japanese_name='tesuto',
            english_name='test anime',
            studio='abc-studios',
            slug_name='test_anime',
            anilist_link='https://www.test.com'
        )
        song = Song(anime=anime, song_type='OP', number='1')
        cls.rating = SongRating(song=song, rating=5, parent_list=cls.user.songlist)

    def test_has_permission_true(self):
        perm = IsOwner()

        request = self.factory.delete('/')
        request.user = self.user
        
        self.assertTrue(perm.has_permission(request, None))
    
    def test_has_permission_false(self):
        perm = IsOwner()

        request = self.factory.delete('/')
        request.user = AnonymousUser()
        
        self.assertFalse(perm.has_permission(request, None))

    def test_has_object_permission_true(self):
        perm = IsOwner()

        request = self.factory.delete('/')
        request.user = self.user
        
        self.assertTrue(perm.has_object_permission(request, None, self.rating))
    
    def test_has_object_permission_false(self):
        perm = IsOwner()
        
        request = self.factory.delete('/')
        request.user = User.objects.create_user('differentuser')
        
        self.assertFalse(perm.has_object_permission(request, None, self.rating))