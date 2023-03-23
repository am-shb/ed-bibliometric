from models.base import Session, engine, Base
from models.article import Article
from models.author import Author
from scholarly import scholarly, ProxyGenerator
from dotenv import load_dotenv
import os

def init():
    load_dotenv()

    pg = ProxyGenerator()
    success = pg.ScraperAPI(os.getenv('SCRAPER_API_KEY'), premium=True)
    scholarly.use_proxy(pg, pg)

    Base.metadata.create_all(engine)

def store_article_generator(article_generator, search_term='', max=-1, main_article=None, session=None):
    close_session = False
    if not session:
        close_session = True
        session = Session()
    i = 0
    for article_dict in article_generator:
        i += 1
        if max !=-1 and i > max:
            print(f'Reached target maximum of {i-1} articles.')
            break
        
        article = Article(article_dict)
        
        duplicate = session.query(Article)\
            .where(Article.scholar_id == article.scholar_id)\
            .first()
        if duplicate:
            print(f'Duplicate article {article.title}')
            if main_article:
                main_article.citations.append(duplicate)
                session.commit()
            continue

        scholarly.fill(article_dict)
        article = Article(article_dict)
        article.search_term = search_term
        article.depth = main_article.depth + 1 if main_article else 0
        article.fetched_citations = 0
        
        author_ids = article_dict['author_id']
        if type(article_dict['bib']['author']) == list:
            author_names = article_dict['bib']['author']
        else:
            author_names = article_dict['bib']['author'].split('and')
        for id, name in zip(author_ids, author_names):
            name = name.strip()
            author = None
            if id != '':
                author = session.query(Author).where(Author.scholar_id == id).first()
            if not author:
                author = session.query(Author).where(Author.name == name).first()
            if not author:
                author = Author(scholar_id=id, name=name)
                session.add(author)

            article.authors.append(author)
            
        session.add(article)
        if main_article:
            main_article.citations.append(article)
        session.commit()
        print(article.title)
        

    if close_session:
        session.close()