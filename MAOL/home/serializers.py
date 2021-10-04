import json

def song_serializer(qs):
    """
    Doesn't do a whole lot, just keeps code readable.

    @qs: A queryset of songs
    """

    return json.dumps(list(qs))