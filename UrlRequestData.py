import requests
import random

class UrlRequestData:
    def __init__(self, url):
        self.url = url
        self.time_array = []
        self.while_loop_counter = 0
        self.random_iterator = random.randint(1, 20)
        self.average_time = 0
        self.maximum_time = 0
        self.minimum_time = 1000
        while self.while_loop_counter < self.random_iterator + 1:
            response = requests.post(url)
            self.time_array.append(response.elapsed.total_seconds())

        for i in self.time_array:
            self.average_time += i
            if i > self.maximum_time:
                self.maximum_time = i
            if i < self.minimum_time:
                self.minimum_time = i
        self.average_time = self.average_time / self.random_iterator

    def __str__(self):
        print (self.url)
        print("\nmin = 0.5d% seconds, max = %0.5d seconds, average = 0.5d% seconds" % self.minimum_time, self.maximum_time, self.average_time)