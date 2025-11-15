# Inspired by alumik/dblp-api
# URL: https://github.com/alumik/dblp-api/blob/main/dblp/api.py

import requests

from urllib.parse import urlencode
from importlib.resources import open_binary

BASE_URL = 'https://dblp.org/search/publ/api'

def search_DBLP(q, max_hits=5) -> list[dict | None]:
    if isinstance(q, (list)):
        queries = q
    elif isinstance(q, (str)):
        queries = [q]

    results = []
    for query in queries:
        options = {
            'q': query,
            'format': 'json',
            'h': max_hits,
        }
        r = requests.get(f'{BASE_URL}?{urlencode(options)}').json()
        if "hit" in r['result']['hits']:
            hit = r['result']['hits']['hit']
            for entry in hit:
                info = entry['info']
                authors_list = info['authors']['author']
                # the authors_list is a list of dictionaries if there are several authors, or a dictionary is there is a single one.
                if isinstance(authors_list, (list)): 
                    info['authors'] = [author['text'] for
                                       author in authors_list]
                else:
                    info['authors'] = authors_list['text']
                results.append(info)
    return results
