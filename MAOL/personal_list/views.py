from django.core.serializers import serialize
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Profile
from home.serializers import song_serializer

def profile(request, id=None):
    # If an id is passed in, display the user's profile (if exists)
    if id:
        id = User.objects.filter(username=id)

        if id.exists():

            # This profile has to stay a queryset to be serialized nicely.
            profile = Profile.objects.filter(user=id[0])
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
        return render(request, 'profile.html')
    # if no user is logged in, redirect to login page
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

