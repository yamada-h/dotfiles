from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import func
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///emoji.db', echo=True)
Session = sessionmaker(bind=engine)

class EmojiList(Base):
    __tablename__ = 'emojilists'

    id = Column(Integer, primary_key=True)
    data = Column(String)
    created_at = Column(DateTime, server_default=func.now())

def main():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    main()
