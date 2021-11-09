from locust import HttpUser, task, between


class HavanUser(HttpUser):
    wait_time = between(1, 10)
    host = 'https://www.havan.com.br'

    @task
    def notebook_asus_task(self):
        self.client.get(
            "/notebook-asus-e510ma-celeron-4gb-128gb-windows-10-pro-diversos/p", name="notebook_asus"
        )

    @task(3)
    def tlou_2_task(self):
        self.client.get(
            "/jogo-the-last-of-us-part-ii-playstation-4-aventura/p", name="the_last_of_us_2"
        )
