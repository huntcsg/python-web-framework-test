from locust import HttpLocust, TaskSet, task


class ReadDisk(TaskSet):
    @task
    def read_disk(self):
        self.client.get("/read-disk", json={'count': 1}, name='/read-disk?count=1')
