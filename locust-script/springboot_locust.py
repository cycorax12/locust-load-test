from locust import HttpUser, task, between #this is self explanatry we importing required classes, function from locust module.

class SpringBootUser(HttpUser): #Simulates a single Real world User. HttpUser class is extended so we provide what task user will do.
    
    '''this wont take effect in our scenario, as this attribute is optional and specify wait time randomly picked between 
    parameters passed (1-3 seconds) between multiple @task executed. We have only one @task executed'''
    wait_time = between(1, 3) 
    
    '''This is main core functionality of locust. @task are treated as a singel http request made. 
    We can multiple have @task. In below we are going to hit /greet endpoint on our localhost'''
    @task
    def hello_world(self):
        self.client.get("/greet")