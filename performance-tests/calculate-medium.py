from locust import HttpLocust, TaskSet, task
import web_framework_test.tasks.calculate


class CalculateMediumLocust(HttpLocust):
    task_set = web_framework_test.tasks.calculate.CalculateMedium
    min_wait = 1000
    max_wait = 1000
