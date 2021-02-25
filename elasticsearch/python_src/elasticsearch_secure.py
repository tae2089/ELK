from elasticsearch import Elasticsearch

def login():
    try:
        es = Elasticsearch(
            "0.0.0.0",
            http_auth=('id', 'password'),
            port=9200
        )
        print("Connected",es.info())
    except Exception as ex:
        print("error",ex)

if __name__ == "__main__":
    main()