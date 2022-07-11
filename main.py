from networking import get_chart_from_lastfm
from models import User


users = ['varvara_kisel']

user = User(name='varvara_kisel')
user.save()

print(User.select())
