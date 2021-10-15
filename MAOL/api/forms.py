from django.forms import ModelForm

from personal_list.models import SongRating


class AddSongRatingForm(ModelForm):
    class Meta:
        model = SongRating
        fields = ['rating', 'parent_list', 'song']
