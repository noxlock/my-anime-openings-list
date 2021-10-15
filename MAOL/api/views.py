import json

from .forms import AddSongRatingForm

from django.http import HttpResponse


def add_to_list(request):
    body = request.body.decode('utf-8')
    body = json.loads(body)
    body['data']['parent_list'] = request.user.songlist.pk

    form = AddSongRatingForm(body['data'])
    if form.is_valid():
        form.save()
        print('SUCCESS')
    else:
        print(form.errors)
    # form.save()

    print(body)
    print(request.user.songlist.pk)
    return HttpResponse(200)
