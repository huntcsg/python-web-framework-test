from locust import HttpLocust, TaskSet, task
import web_framework_test.tasks.deserialize


class DeserializeLocust(HttpLocust):
    task_set = web_framework_test.tasks.deserialize.Deserialize
    min_wait = 1000
    max_wait = 1000
