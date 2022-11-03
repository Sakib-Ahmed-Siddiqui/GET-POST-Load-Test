from locust import HttpUser, between, task
import json
from threading import Thread



class WebsiteUser(HttpUser):
    #wait_time = between(5, 15)
    
    def thread_1(self):
        self.client.post("localhost:8000", {
            
        })
    
    @task
    def index_1(self):
        self.client.post("/")
        



