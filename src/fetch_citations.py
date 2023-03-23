from models.base import Session
from models.article import Article
from utils import init, store_article_generator
from scholarly import scholarly

init()

session = Session()

articles = session.query(Article)\
    .where(Article.fetched_citations == 0)\
    .where(Article.depth == 0)\
    .all()

for article in articles:
    citing_articles = scholarly.search_pubs_custom_url(article.citedby_url)
    store_article_generator(citing_articles, f'citations of "{article.title}"', main_article=article, session=session)
    article.fetched_citations = 1
    session.commit()
    print(f'-------- Fetched all citations of "{article.title}"')

session.close()