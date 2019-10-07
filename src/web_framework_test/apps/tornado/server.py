from .app import get_app
import logging
import tornado.ioloop
import tornado.web
import tornado.httpserver


def get_server(workers=1):

    application = get_app()
    server = tornado.httpserver.HTTPServer(application)
    server.bind(6543)

    logging.info("Number of workers: {}".format(workers))
    server.start(workers)

    return server


if __name__ == '__main__':
    import sys

    workers = int(sys.argv[1])

    server = get_server(workers=workers)

    # access_log = logging.getLogger('tornado.access')
    # app_log = logging.getLogger('tornado.application')
    # tornado_log = logging.getLogger('tornado.general')
    #
    # loggers = [access_log, app_log, tornado_log]
    # handler = logging.StreamHandler()
    #
    # for logger in loggers:
    #     logger.addHandler(handler)
    #     logger.setLevel(logging.INFO)

    tornado.ioloop.IOLoop.current().start()
