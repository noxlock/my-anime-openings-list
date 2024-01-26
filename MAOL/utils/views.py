
def get_list(request):
    """
    Any screen that allows users to add to their list requires their list to
    be passed to the template. Since we do this a lot, this is just a shorthand
    to handle the case of Anonymous users.

    @request: Django HttpRequest object
    """

    if request.user.is_anonymous:
        return None
    return request.user.songlist.pk