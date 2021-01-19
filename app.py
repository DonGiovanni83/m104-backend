import tornado.web
from tornado.ioloop import IOLoop

from graphene_tornado.tornado_graphql_handler import TornadoGraphQLHandler

from api.schema import schema


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/graphql', TornadoGraphQLHandler, dict(graphiql=False, schema=schema)),
            (r'/graphiql', TornadoGraphQLHandler, dict(graphiql=True, schema=schema))
        ]
        tornado.web.Application.__init__(self, handlers)


if __name__ == '__main__':
    app = Application()
    app.listen(9000)
    IOLoop.instance().start()
