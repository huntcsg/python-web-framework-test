from locust import HttpLocust, TaskSet, task


class ReadNetwork(TaskSet):
    @task
    def read_network(self):
        self.client.get("/read-network", json={'count': 1}, name='/read-network?count=1')
