from net.net import get_chart_from_lastfm
from db.models import User
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

users = ['varvara_kisel']

user = User(name='varvara_kisel')
user.save()

print(User.select())
