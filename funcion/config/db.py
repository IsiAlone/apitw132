from sqlalchemy import create_engine, MetaData

''''
```
engine = create_engine('<packages>://<databaseUser>:<databasePassword>@localhost:<port>/<your database name>', 
pool_pre_ping = True(checks that database is connected))
```
'''
engine = create_engine('mysql+pymysql://root:123@localhost:8080/apitwitter132', pool_pre_ping=True)

meta = MetaData()

conn = engine.connect()
