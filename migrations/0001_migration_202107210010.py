# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Track(peewee.Model):
    name = CharField(max_length=255)
    url = CharField(max_length=255)
    class Meta:
        table_name = "track"


@snapshot.append
class Chart(peewee.Model):
    track_id = snapshot.ForeignKeyField(backref='charts', index=True, model='track')
    final_position = IntegerField()
    date = DateField()
    class Meta:
        table_name = "chart"


@snapshot.append
class User(peewee.Model):
    lastfm_login = CharField(max_length=255, unique=True)
    vk_url = CharField(max_length=255)
    class Meta:
        table_name = "user"


@snapshot.append
class UserTrack(peewee.Model):
    user_id = snapshot.ForeignKeyField(backref='tracks', index=True, model='user')
    track_id = snapshot.ForeignKeyField(backref='users', index=True, model='track')
    date = DateField()
    playcount = IntegerField()
    rate = FloatField()
    class Meta:
        table_name = "usertrack"


