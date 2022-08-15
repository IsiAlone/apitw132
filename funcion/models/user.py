from datetime import date
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String,Date
from config.db import meta, engine

tweets = Table('tweet',meta, Column('fecha', Date), Column('cuenta', String(255)), Column('clave', String(255)), Column('tw_id', String(255), primary_key=True), Column('tw_content', String(255)))


meta.create_all(engine)