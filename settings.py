method = 'user.gettoptracks'

api_key = ''
limit = 10
period = '7day'


def get_url(user):
    url = f'http://ws.audioscrobbler.com/2.0/?method={method}&user={user}' \
        f'&api_key={api_key}&format=json&limit={limit}&period={period}'
    return url
