from locust import HttpLocust, TaskSet, task


class Deserialize(TaskSet):
    @task
    def deserialize(self):
        self.client.get("/deserialize", json={'count': 10}, name='/deserialize?count=10')
