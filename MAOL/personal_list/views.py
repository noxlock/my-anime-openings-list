from django.core.serializers import serialize
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Profile
from home.serializers import song_serializer


def profile(request, id=None):
    # If an id is passed in, display the user's profile (if exists)
    if id:
        user = User.objects.filter(username=id)

        if user.exists():

            # This profile has to stay a queryset to be serialized nicely.
            profile = Profile.objects.filter(user=user[0])
            json_profile = serialize('json', profile)

            # Get the top rated, and recently rated songs of the user,
            # Serializing the querysets as well.
            topRated = song_serializer(profile[0].get_top_ratings(20))
            # recentRated = song_serializer(profile[0].get_recent_ratings(20))

            context = {'profile': json_profile, 'topRated': topRated}

            return render(request, 'profile.html', context)

        # If no user was found, display an error
        else:
            return render(request, 'profile_error.html', {'id': id})

    # if an id is not given, try displaying the logged in user's profile
    elif not id and request.user.is_authenticated:
        return redirect(f'/profile/{request.user.username}')

    # if no user is logged in, redirect to login page
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


def list(request, id=None):
    user = User.objects.filter(username=id)

    if user.exists():
        profile = Profile.objects.filter(user=user[0])

        ratings = song_serializer(profile[0].get_rated_songs())
        json_profile = serialize('json', profile)

        # Pass the following to the template:
        # profile (for banner & picture)
        # ratings (for their list)
        # id (for certain display conditions)
        context = {'profile': json_profile, 'ratings': ratings, 'id': id}
        return render(request, 'list.html', context)

    else:
        return render(request, 'profile_error.html', {'id': id})
