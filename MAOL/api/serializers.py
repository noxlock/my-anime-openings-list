from rest_framework import serializers

from personal_list.models import SongRating

class SongRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongRating
        fields = ['song', 'parent_list', 'rating']

