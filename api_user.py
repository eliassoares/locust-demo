from locust import HttpUser, task, between


class APIUser(HttpUser):
    wait_time = between(1, 10)
    host = 'http://api:5000'

    @task(2)
    def test_user_route(self):
        self.client.get('/user')

    @task(1)
    def test_access_route(self):
        self.client.get('/access')
