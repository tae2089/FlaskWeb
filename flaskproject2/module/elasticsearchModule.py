from elasticsearch import Elasticsearch

class Elastic:
        def __init__(self):
            try:
                self.es = Elasticsearch("13.209.166.58",
                            http_auth=("elastic","haniumelk@!"),
                            port=9200 )
            except Exception as ex:
                print("error:",ex)

        def searchAPI(self):
            index = 'test2'
            body = {'size':2}
            res = self.es.search(index=index, body=body)
            print(res)
            return res
