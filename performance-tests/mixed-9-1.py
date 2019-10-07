from locust import HttpLocust, TaskSet, task
import web_framework_test.tasks.deserialize
import web_framework_test.tasks.calculate


class DeserializeLocust(HttpLocust):
    weight = 9
    task_set = web_framework_test.tasks.deserialize.Deserialize
    min_wait = 1000
    max_wait = 1000


class CalculateMediumLocust(HttpLocust):
    weight = 1
    task_set = web_framework_test.tasks.calculate.CalculateMedium
    min_wait = 1000
    max_wait = 1000
