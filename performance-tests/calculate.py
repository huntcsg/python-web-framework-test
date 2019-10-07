from locust import HttpLocust, TaskSet, task
import web_framework_test.tasks.calculate


class CalculateLongLocust(HttpLocust):
    task_set = web_framework_test.tasks.calculate.Calculatelong
    min_wait = 1000
    max_wait = 1000


class CalculateShortLocust(HttpLocust):
    task_set = web_framework_test.tasks.calculate.CalculateShort
    min_wait = 1000
    max_wait = 1000


class CalculateMediumLocustt(HttpLocust):
    task_set = web_framework_test.tasks.calculate.CalculateMedium
    min_wait = 1000
    max_wait = 1000
