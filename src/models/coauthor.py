# from sqlalchemy import *
# from sqlalchemy.orm import relationship

# from models.base import Base


# class Coauthor(Base):
#     __tablename__ = 'coauthors'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     author_id = Column(Integer, ForeignKey('authors.id'))
#     scholar_id = Column(String)
#     fullname = Column(String)
#     affiliation = Column(String)
    
#     author = relationship("Author", back_populates="coauthors")
    
#     def fill_from_dict(self, coauthor_dict: dict):
#         self.scholar_id = author_dict.get('scholar_id', '')
#         self.fullname = author_dict.get('name', '')
#         self.affiliation = author_dict.get('affiliation', '')
    