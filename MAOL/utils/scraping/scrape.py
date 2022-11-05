import requests
import time

from django.utils.text import slugify

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
                coverImage {
                    large
                }
                seasonYear
            }
        }
    }
    """

    responses = []

    while pages > 0:
        variables = {
            'page': pages
        }
        r = requests.post(
            "https://graphql.anilist.co",
            json={'query': q, 'variables': variables}
        )
        responses.append(r.json())
        pages -= 1

    for response in responses:
        for media in response['data']['Page']['media']:

            japanese_name = media['title']['romaji']
            english_name = media['title']['english']
            slug_name = slugify(japanese_name).replace('-', '_')

            if Anime.objects.filter(slug_name=slug_name).exists():
                slug_name += f"_{media['seasonYear']}"

            Anime.objects.update_or_create(
                japanese_name=japanese_name.title(),
                # API results can have a null english name
                english_name=english_name if english_name else japanese_name,
                slug_name=slug_name,
                studio=media['studios']['nodes'][0]['name'],
                anilist_link=media['siteUrl'],
                cover=media['coverImage']['large']
            )


def get_videos(name):

    anime = Anime.objects.filter(slug_name=name)

    if anime.count() > 1:
        raise ValueError(f'duplicate slug {name}')

    # for some reason, their API blocks the `requests` user agent,
    # so set a random one
    headers = {
        'user-agent': "MAOL"
    }
    include = '?include=animethemes.animethemeentries.videos'
    url = 'https://staging.animethemes.moe/api/anime/{0}{1}'

    r = requests.get(url.format(name, include), headers=headers)
    r = r.json()

    # either the anime name from anilist doesn't match up,
    # or the anime doesn't have an entry.
    if r.get('message'):
        raise ValueError(f'Anime not found: {name}')

    for theme in r['anime']['animethemes']:
        if theme['type'] not in ['OP', 'ED']:
            continue

        # At the time of writing, playback is disabled on the staging server
        video_link = theme['animethemeentries'][0]['videos'][0]['link'].replace('staging.', '')  # noqa: E501

        # The `sequence` is sometimes null, so we have to dig deeper for it
        number = video_link.replace('.webm', '').split('-')[1][2:]

        detail_link = f"/song/{name}-{theme['type']}-{number}"
        Song.objects.get_or_create(
            anime=anime[0],
            song_type=theme['type'],
            number=number,
            detail_link=detail_link,
            defaults={'video_link': video_link}
        )


def get_songs(name):

    anime = Anime.objects.filter(slug_name=name)

    if anime.count() > 1:
        raise ValueError(f'duplicate slug {name}')

    # for some reason, their API blocks the `requests` user agent,
    # so set a random one
    headers = {
        'user-agent': "MAOL"
    }
    include = '?include=animethemes.song'
    url = 'https://staging.animethemes.moe/api/anime/{0}{1}'

    r = requests.get(url.format(name, include), headers=headers)
    r = r.json()

    # either the anime name from anilist doesn't match up,
    # or the anime doesn't have an entry.
    if r.get('message'):
        raise ValueError(f'Anime not found: {name}')

    for theme in r['anime']['animethemes']:

        if theme['type'] not in ['OP', 'ED']:
            continue

        if theme['sequence']:
            sequence = theme['sequence']
        else:
            sequence = 1

        # print(f"Song: {theme['song']['title']} {theme['type']}{sequence}\n")

        song = Song.objects.get(
            anime__slug_name=anime[0].slug_name,
            song_type=theme['type'],
            number=sequence,
        )
        song.name = theme['song']['title']
        song.save()


def create_all_songs():
    """
    Get all the songs relating to anime series we've grabbed.
    Create a `Song` model for each.
    """

    for anime in Anime.objects.all():
        # rate limit is 60/min
        time.sleep(2)

        print(anime.slug_name)

        try:
            get_videos(anime.slug_name)
            get_songs(anime.slug_name)
        # if the anime name doesn't match up, skip it.
        except ValueError as e:
            print(e)
            continue


def get_all(pages=5):
    get_anime(pages)
    create_all_songs()
