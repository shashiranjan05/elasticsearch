
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search
connections.create_connection()

from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

class BlogPostIndex(DocType):
    author = Text()
    posted_date = Date()
    title = Text()
    text = Text()

    class Meta:
        index = 'blogpost-index'


def bulk_indexing():
    BlogPostIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.BlogPost.objects.all().iterator()))

def search(title):
    s = Search().filter('term', title=title)
    response = s.execute()
    return response


