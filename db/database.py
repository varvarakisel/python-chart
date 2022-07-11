from peewee import PostgresqlDatabase


db = PostgresqlDatabase('chart', user='user', password='123#!', host='localhost', port=5432)
