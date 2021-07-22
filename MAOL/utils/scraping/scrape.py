import re
import requests
import time

from home.models import Anime, Song


def get_anime(pages=1):
    """
    Get a list of popular anime from anilist.
    Create an `Anime` model for each.

    @pages: How many pages of data to get (default 1)
    """

    q = """
    query ($page: Int) {
        Page (page: $page, perPage: 50) {
            media (type: ANIME sort: POPULARITY_DESC) {
                title {
                    romaji
                    english
                }
                studios (isMain: true) {
                    nodes {
                        name
                    }
                }
            siteUrl
            }
        }
    }
    """

    responses = []

    while pages > 0:
        variables = {
            'page': pages
        }
        r = requests.post("https://graphql.anilist.co", json={'query': q, 'variables': variables})
        responses.append(r.json())
        pages -= 1

    for response in responses:
        for media in response['data']['Page']['media']:

            japanese_name = media['title']['romaji']
            english_name = media['title']['english']

            Anime.objects.update_or_create(
                japanese_name=japanese_name,
                # API results can have a null english name
                english_name=english_name if english_name else japanese_name,
                studio=media['studios']['nodes'][0]['name'],
                anilist_link=media['siteUrl']
            )


def get_song(anime):

    # for some reason, their API blocks the `requests` user agent
    headers = {
        'user-agent': "MAOL"
    }
    url = f'https://staging.animethemes.moe/api/anime/{anime}?include=themes.entries.videos'

    # format anime name to animethemes `slug`
    name = re.sub(r'\W+', ' ', anime.japanese_name)
    name = name.lower().replace(' ', '_')

    r = requests.get(url.format(name), headers=headers)
    r = r.json()

    # either the anime name from anilist doesn't match up,
    # or the anime doesn't have an entry. just skip it.
    if r.get('errors'):
        return 'Anime not found'

    for theme in r['anime']['themes']:
        # At the time of writing, playback is disabled on the staging server
        video_link = theme['entries'][0]['videos'][0]['link'].replace('staging.', '')

        # The `sequence` is sometimes null, so we have to dig deeper for it
        number = video_link.replace('.webm', '').split('-')[1][2:]

        Song.objects.update_or_create(
            song_type=theme['type'],
            number=number,
            video_link=video_link,
            anime=anime
        )


def get_all_songs():
    """
    Get all the songs relating to anime series we've grabbed.
    Create a `Song` model for each.
    """

    for anime in Anime.objects.all():
        # rate limit is 60/min
        time.sleep(1)
        print(anime)
        get_song(anime)
