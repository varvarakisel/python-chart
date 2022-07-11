import requests
from collections import namedtuple

from settings import get_url


JsonTrack = namedtuple('JsonTrack', ['name', 'playcount'])


def get_chart_from_lastfm(user):
    url = get_url(user)
    r = requests.get(url)

    if r.status_code == 200:
        chart = r.json()['toptracks']
        tracks = chart['track']

        json_tracks = []
        for track in tracks:
            print(track.__dict__)
            json_tracks.append(JsonTrack(track['name'], track['playcount']))

        return json_tracks
    return []
