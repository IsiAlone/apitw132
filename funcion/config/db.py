from sqlalchemy import create_engine, MetaData


engine = create_engine('mysql+pymysql://root:123@localhost:8080/apitwitter132', pool_pre_ping=True)

meta=MetaData()

conn= engine.connect()

