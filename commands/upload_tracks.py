from models import User, Track, UserTrack
from networking import get_chart_from_lastfm


def upload_tracks():
    ''' Для каждого пользователя загружаем недельный чарт,
        песням назначаем баллы и сохраняем данные в таблице
        
    '''
    users = User.select()

    for user in users:
        tracks = get_chart_from_lastfm(user.lastfm_login)

        for track in tracks:
            pass