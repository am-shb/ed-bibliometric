from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

_DB_URI = 'sqlite:///db.sqlite'
engine = create_engine(_DB_URI)
Session = sessionmaker(bind=engine)

Base = declarative_base()