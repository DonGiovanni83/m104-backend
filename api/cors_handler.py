from graphene_tornado.tornado_graphql_handler import TornadoGraphQLHandler


class CORSHandler(TornadoGraphQLHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header('Access-Control-Allow-Methods', 'POST, PUT, GET, OPTIONS')
        self.set_header('Access-Control-Allow-Headers', 'content-type')

    def options(self):
        self.finish()
