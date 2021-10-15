import json


def song_serializer(qs):
    """
    Doesn't do a whole lot, just helps keep code readable.

    Vue doesn't play nice with pure querysets, so we need to serialize them.

    @qs: A queryset of songs
    """

    return json.dumps(list(qs))
