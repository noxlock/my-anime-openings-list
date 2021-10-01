from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def profile(request, id=None):
    # If an id is passed in, display the user's profile (if exists)
    if id:
        user = User.objects.filter(username=id)
        if user.exists():
            context = {'user': user[0]}
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

