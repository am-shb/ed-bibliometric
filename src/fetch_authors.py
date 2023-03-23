from models.base import Session, engine, Base
from models.article import Article
from models.author import Author
from utils import init
from scholarly import scholarly

init()

session = Session()

authors = session.query(Author)\
    .where(Author.affiliation == None)\
    .where(Author.scholar_id != '')\
    .all()

for author in authors:
    author_dict = scholarly.search_author_id(author.scholar_id)
    scholarly.fill(author_dict, sections=['basics', 'indices', 'coauthors'])
    author.fill_from_dict(author_dict)
    session.commit()
    print(author.name)
    
    

session.close()