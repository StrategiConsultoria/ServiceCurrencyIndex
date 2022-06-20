from threading import Thread


class RunningScrape():
    def __init__(self):
        self.runnings = 0
        self.response = {}
        self.calls = []
    def join(self,scrape,name):
        self.calls.append({'scrape':scrape,'name':name})
        self.response[name] = []

    def running(self,scrape,name):
        self.runnings += 1
        for row in scrape.start():
            self.response[name].append(row)
        self.runnings -= 1

    def start(self):
        for scrape in self.calls:
            Thread(target=self.running,args=[scrape['scrape'],scrape['name']]).start()
        while self.runnings > 0:
            ...
        return self.response
        
