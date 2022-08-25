from peewee import Model, CharField, IntegerField, ForeignKeyField, DateField, FloatField

from db.database import db


class User(Model):
    lastfm_login = CharField(unique=True)
    tg_url = CharField()

    class Meta:
        database = db


class Track(Model):
    name = CharField()
    url = CharField()

    class Meta:
        database = db


class Chart(Model):
    track_id = ForeignKeyField(Track, backref='charts')
    final_position = IntegerField()
    date = DateField()

    class Meta:
        database = db


class UserTrack(Model):
    user_id = ForeignKeyField(User, backref='tracks')
    track_id = ForeignKeyField(Track, backref='users')
    date = DateField()
    playcount = IntegerField()
    rate = FloatField()

    class Meta:
        database = db
