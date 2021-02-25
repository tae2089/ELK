from elasticsearch import Elasticsearch
from datetime import datetime
class elasticsearch_code:

    def insertData():
        es = Elasticsearch('localhost:9200')

        index="product_list"

        doc = {
            "category" : "skirt",
            "c_key" : "1234",
            "price" : 11400,
            "status" : 1,
            "@timestamp" : datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
            }

        es.index(index="product_list", doc_type="_doc", body=doc)

    def insertDataMappingJson():
        es = Elasticsearch('localhost:9200')

        index="product_list"

        with open('mapping.json', 'r') as f:
            mapping = json.load(f)

        es.indices.create(index=index, body=mapping)

        doc = {
            "category" : "skirt",
            "c_key" : "1234",
            "price" : 11400,
            "status" : 1,
            "@timestamp" : datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
            }

        es.index(index="product_list", doc_type="_doc", body=doc)


    def searchAPI():
        es = Elasticsearch('localhost:9200')

        index = 'product_list'
        body = ''
        res = es.search(index=index, body=body)
        print(res)


    def login():
    try:
        es = Elasticsearch(
            "0.0.0.0",
            http_auth=('id', 'password'),
            port=9200
        )
        print("Connected", es.info())
    except Exception as ex:
        print("error", ex)
