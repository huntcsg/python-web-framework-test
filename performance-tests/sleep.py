from locust import HttpLocust, TaskSet, task
import web_framework_test.tasks.sleep


class SleepLocust(HttpLocust):
    task_set = web_framework_test.tasks.sleep.Sleep
    min_wait = 1000
    max_wait = 1000
