from locust import HttpLocust, TaskSet, task
from web_framework_test import tasks
import web_framework_test.tasks.deserialize
import web_framework_test.tasks.read_disk
import web_framework_test.tasks.read_network
import web_framework_test.tasks.calculate


class CalculateLongLocust(HttpLocust):
    weight = 2
    task_set = web_framework_test.tasks.calculate.Calculatelong
    min_wait = 1000
    max_wait = 1000


class CalculateShortLocust(HttpLocust):
    weight = 10
    task_set = web_framework_test.tasks.calculate.CalculateShort
    min_wait = 1000
    max_wait = 1000


class CalculateMediumLocustt(HttpLocust):
    weight = 5
    task_set = web_framework_test.tasks.calculate.CalculateMedium
    min_wait = 1000
    max_wait = 1000


class DeserializeLocust(HttpLocust):
    weight = 20
    task_set = web_framework_test.tasks.deserialize.Deserialize
    min_wait = 1000
    max_wait = 1000


class ReadDiskLocust(HttpLocust):
    weight = 5
    task_set = web_framework_test.tasks.read_disk.ReadDisk
    min_wait = 1000
    max_wait = 1000


class ReadNetworkLocust(HttpLocust):
    weight = 5
    task_set = web_framework_test.tasks.read_network.ReadNetwork
    min_wait = 1000
    max_wait = 1000
