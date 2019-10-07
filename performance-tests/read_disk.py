from locust import HttpLocust, TaskSet, task
import web_framework_test.tasks.read_disk


class ReadDiskLocust(HttpLocust):
    task_set = web_framework_test.tasks.read_disk.ReadDisk
    min_wait = 1000
    max_wait = 1000
