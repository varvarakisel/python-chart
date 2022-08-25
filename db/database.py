from peewee import PostgresqlDatabase


db = PostgresqlDatabase('chart', user='postgres',
                        password='postgres', host='localhost', port=5432)
