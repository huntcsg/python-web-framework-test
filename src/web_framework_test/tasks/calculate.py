from locust import HttpLocust, TaskSet, task


class CalculateShort(TaskSet):
    weight = 20
    @task
    def calculate_short(self):
        self.client.get("/calculate", json={'count': 10}, name='/calculate?count=10')


class CalculateMedium(TaskSet):
    weight = 5
    @task
    def calculate_medium(self):
        self.client.get("/calculate", json={'count': 30}, name='/calculate?count=30')


class Calculatelong(TaskSet):
    weight = 1
    @task
    def calculate_long(self):
        self.client.get("/calculate", json={'count': 35}, name='/calculate/?count=35')
