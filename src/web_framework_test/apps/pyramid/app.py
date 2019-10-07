from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
from pyramid.response import Response
from web_framework_test import routines


@view_config(route_name="calculate", renderer="json")
def calculate(request):
    count = request.json_body["count"]
    return {"result": routines.calculate(count)}


@view_config(route_name="read-network", renderer="json")
def read_network(request):
    count = request.json_body["count"]
    return {"result": routines.read_network(count)}


@view_config(route_name="read-disk", renderer="json")
def read_disk(request):
    count = request.json_body["count"]
    return {"result": routines.read_disk(count)}


@view_config(route_name="deserialize", renderer="json")
def deserialize(request):
    count = request.json_body["count"]
    return {"result": routines.deserialize(count)}


@view_config(route_name="sleep", renderer="json")
def sleep(request):
    count = request.json_body["count"]
    return {"result": routines.sleep(count)}


def make_app():
    config = Configurator()

    config.add_route("calculate", "/calculate")
    config.add_route("read-network", "/read-network")
    config.add_route("read-disk", "/read-disk")
    config.add_route("deserialize", "/deserialize")
    config.add_route("sleep", "/sleep")

    config.scan()

    return config.make_wsgi_app()

app = make_app()
