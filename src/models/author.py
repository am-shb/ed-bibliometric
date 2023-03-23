from sqlalchemy import *
from sqlalchemy.orm import relationship

from models.base import Base


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    scholar_id = Column(String)
    name = Column(String)
    fullname = Column(String)
    affiliation = Column(String)
    url_picture = Column(String)
    interests = Column(String)
    hindex = Column(Integer)
    hindex5y = Column(Integer)
    i10index = Column(Integer)
    i10index5y = Column(Integer)
    citedby = Column(Integer)
    citedby5y = Column(Integer)
    email_domain = Column(String)
    coauthors = Column(Text)
    
    
    def fill_from_dict(self, author_dict: dict):
        self.fullname = author_dict.get('name', '')
        self.affiliation = author_dict.get('affiliation', '')
        self.url_picture = author_dict.get('url_picture', '')
        self.interests = ', '.join(author_dict.get('interests', ''))
        self.hindex = author_dict.get('hindex', '')
        self.hindex5y = author_dict.get('hindex5y', '')
        self.i10index = author_dict.get('i10index', '')
        self.i10index5y = author_dict.get('i10index5y', '')
        self.citedby = author_dict.get('citedby', '')
        self.citedby5y = author_dict.get('citedby5y', '')
        self.email_domain = author_dict.get('email_domain', '')
        self.coauthors = str(author_dict.get('coauthors', ''))
    