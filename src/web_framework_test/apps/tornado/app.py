import tornado.ioloop
import tornado.web
import tornado.httpserver

import logging

import json
from web_framework_test import routines


class BaseHandler(tornado.web.RequestHandler):
    def prepare(self):
        if self.request.headers["Content-Type"] == "application/json":
            self.args = json.loads(self.request.body)


class Calculate(BaseHandler):
    def get(self):
        count = self.args["count"]
        result = routines.calculate(count)
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps({"result": result}))


class ReadDisk(BaseHandler):
    def get(self):
        count = self.args["count"]
        result = routines.read_disk(count)

        self.set_header("Content-Type", "application/json")
        self.write(json.dumps({"result": result}))


class Deserialize(BaseHandler):
    def get(self):
        count = self.args["count"]
        result = routines.deserialize(count)

        self.set_header("Content-Type", "application/json")
        self.write(json.dumps({"result": result}))


class ReadNetwork(BaseHandler):
    def get(self):
        count = self.args["count"]
        result = routines.read_network(count)

        self.set_header("Content-Type", "application/json")
        self.write(json.dumps({"result": result}))


class Sleep(BaseHandler):
    def get(self):
        count = self.args["count"]
        result = routines.sleep(count)

        self.set_header("Content-Type", "application/json")
        self.write(json.dumps({"result": result}))


def get_app():
    application = tornado.web.Application(
        [
            (r"/calculate", Calculate),
            (r"/read-disk", ReadDisk),
            (r"/deserialize", Deserialize),
            (r"/read-network", ReadNetwork),
            (r"/sleep", Sleep),
        ]
    )

    return application
