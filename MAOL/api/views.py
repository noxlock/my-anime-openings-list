import json

from .forms import AddSongRatingForm

from django.http import HttpResponse

from personal_list.models import SongRating


def add_to_list(request):
    body = request.body.decode('utf-8')
    body = json.loads(body)
    body['data']['parent_list'] = request.user.songlist.pk

    form = AddSongRatingForm(body['data'])
    if form.is_valid():
        form.save()
        return HttpResponse(status=201)
    else:
        return HttpResponse(form.errors.as_json(), status=200)


def delete_from_list(request):
    body = request.body.decode('utf-8')
    body = json.loads(body)

    rating = SongRating.objects.filter(
        song=body['data']['song'],
        parent_list=request.user.songlist
    )

    if rating.exists():
        rating.delete()
    else:
        return HttpResponse("Song Rating does not exist.", status=404)
    return HttpResponse("Rating deleted successfully!", status=200)


def edit_rating(request):
    body = request.body.decode('utf-8')
    body = json.loads(body)

    # use .get() here, since we'll need to
    # grab the object from the queryset anyway, to change the value
    try:
        rating = SongRating.objects.get(
            song=body['data']['song'],
            parent_list=request.user.songlist
        )
        rating.rating = body['data']['new_rating']
        rating.save()
        return HttpResponse("Rating updated successfully!", status=200)
    except SongRating.DoesNotExist:
        return HttpResponse("Error updating rating.", status=404)
