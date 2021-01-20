from tornado.ioloop import IOLoop
from tornado.web import Application

from api.cors_handler import CORSHandler
from api.schema import schema
from persistence import database


async def main():
    # setup db
    await database.init_db()
    handlers = [
        (r'/graphql', CORSHandler, dict(graphiql=False, schema=schema)),
        (r'/graphiql', CORSHandler, dict(graphiql=True, schema=schema))
    ]

    app = Application(handlers=handlers)
    app.listen(9000)


if __name__ == '__main__':
    mainloop = IOLoop.current()
    mainloop.spawn_callback(main)
    mainloop.start()
