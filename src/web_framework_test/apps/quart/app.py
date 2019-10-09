from quart import Quart, request

from web_framework_test import routines

app = Quart(__name__)

@app.route('/calculate')
async def calculate():
    data = await request.get_json()
    count = data["count"]
    return {"result": routines.calculate(count)}


@app.route('/read-network')
async def read_network():
    data = await request.get_json()
    count = data["count"]
    return {"result": routines.read_network(count)}


@app.route('/read-disk')
async def read_disk():
    data = await request.get_json()
    count = data["count"]
    return {"result": routines.read_disk(count)}


@app.route('/deserialize')
async def deserialize():
    data = await request.get_json()
    count = data["count"]
    return {"result": routines.deserialize(count)}

@app.route('/sleep')
async def sleep():
    data = await request.get_json()
    count = data["count"]
    return {"result": routines.sleep(count)}

