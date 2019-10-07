import json
import os
import requests
import random
import time


HERE = os.path.dirname(__file__)


with open(os.path.join(HERE, "data", "data.json"), "r") as f:
    DATA = f.read()

MILLISECOND_WAIT_TIMES = (
    [5] * 1 +
    [10] * 1 +
    [25] * 5 +
    [50] * 5 +
    [100] * 10 +
    [200] * 5 +
    [500] * 1
)


def calculate(n=1):
    if n <= 2:
        return 1
    else:
        return calculate(n - 1) + calculate(n - 2)


def read_disk(n=1):
    result = []
    for _ in range(n):
        with open(os.path.join(HERE, "data.json"), "r") as f:
            result.append(f.read())
    return result


def deserialize(n=1):
    result = []
    for _ in range(n):
        result.append(json.loads(DATA))
    return result


def read_network(n=1):
    result = []
    for _ in range(n):
        result.append(
            requests.get("https://api.pro.coinbase.com/products/ETH-USD/trades").json()
        )

    return result


def sleep(n=1):
    wait_time = random.choice(MILLISECOND_WAIT_TIMES)
    time.sleep(wait_time / 1000)
    return {'ok': True}
