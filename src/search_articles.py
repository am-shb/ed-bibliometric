from utils import init, store_article_generator
from scholarly import scholarly

init()

search_terms = [
    '"emergency department" machine learning', # 72,000 results
    # '"emergency department" deep learning',    # 67,100 results
    # '"emergency department" prediction model', # 277,000 results
]

for search_term in search_terms:
    search_query = scholarly.search_pubs(
        query=search_term,
        patents=False,
        citations=False,
        year_low=2012,
        year_high=2022,
        start_index=420
    )

    store_article_generator(search_query, search_term, max=720)