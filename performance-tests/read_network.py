from locust import HttpLocust, TaskSet, task
import web_framework_test.tasks.read_network


class ReadNetworkLocust(HttpLocust):
    task_set = web_framework_test.tasks.read_network.ReadNetwork
    min_wait = 1000
    max_wait = 1000
