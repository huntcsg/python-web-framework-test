from locust import HttpLocust, TaskSet, task


class Sleep(TaskSet):
    @task
    def read_network(self):
        self.client.get("/sleep", json={'count': 1}, name='/sleep?count=1')
