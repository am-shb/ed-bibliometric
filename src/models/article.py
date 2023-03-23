from sqlalchemy import *
from sqlalchemy.orm import relationship
from urllib.parse import urlparse, parse_qs

from models.base import Base


citations_table = Table(
    'citations', Base.metadata,
    Column('src_article_id', Integer, ForeignKey('articles.id')),
    Column('ref_article_id', Integer, ForeignKey('articles.id')),
    UniqueConstraint('src_article_id', 'ref_article_id', name='unique_citations')
)

article_author_table = Table(
    'article_author', Base.metadata,
    Column('article_id', Integer, ForeignKey('articles.id')),
    Column('author_id', Integer, ForeignKey('authors.id')),
    UniqueConstraint('article_id', 'author_id', name='unique_authorship')
)

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    scholar_id = Column(String)
    title = Column(String)
    abstract = Column(Text)
    bib_id = Column(String)
    journal = Column(String)
    number = Column(Integer)
    pages = Column(String)
    pub_type = Column(String)
    pub_year = Column(Integer)
    publisher = Column(String)
    venue = Column(String)
    volume = Column(Integer)
    num_citations = Column(Integer)
    gsrank = Column(Integer)
    citedby_url = Column(String)
    eprint_url = Column(String)
    pub_url = Column(String)
    url_add_sclib = Column(String)
    url_related_articles = Column(String)
    url_scholarbib = Column(String)
    search_term = Column(String)
    depth = Column(Integer)
    fetched_citations = Column(Integer)

    authors = relationship('Author', secondary=article_author_table, backref='articles_authors')
    citations = relationship('Article', secondary=citations_table,
                             primaryjoin=id==citations_table.c.src_article_id,
                             secondaryjoin=id==citations_table.c.ref_article_id
    )

    def __init__(self, article: dict):
        parsed_url = urlparse(article.get('url_scholarbib', ''))
        if parsed_url.query:
            qs = parse_qs(parsed_url.query)
            self.scholar_id = qs['q'][0].split(':')[1]
        
        self.abstract = article['bib'].get('abstract', '')
        self.bib_id = article['bib'].get('bib_id', '')
        self.journal = article['bib'].get('journal', '')
        self.number = article['bib'].get('number', '')
        self.pages = article['bib'].get('pages', '')
        self.pub_type = article['bib'].get('pub_type', '')
        self.pub_year = article['bib'].get('pub_year', '')
        self.publisher = article['bib'].get('publisher', '')
        self.title = article['bib'].get('title', '')
        self.venue = article['bib'].get('venue', '')
        self.volume = article['bib'].get('volume', '')
        self.citedby_url = article.get('citedby_url', '')
        self.eprint_url = article.get('eprint_url', '')
        self.gsrank = article.get('gsrank', '')
        self.num_citations = article.get('num_citations', '')
        self.pub_url = article.get('pub_url', '')
        self.url_add_sclib = article.get('url_add_sclib', '')
        self.url_related_articles = article.get('url_related_articles', '')
        self.url_scholarbib = article.get('url_scholarbib', '')
