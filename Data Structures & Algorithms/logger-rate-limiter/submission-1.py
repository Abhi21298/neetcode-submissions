from threading import Lock

class Logger:

    def __init__(self, num_shards = 4):
        self.logger = {}
        self.locks = [Lock() for _ in range(num_shards)]
        self.shards = num_shards 


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        with self.locks[hash(message) % self.shards]:

            if message not in self.logger or self.logger[message] + 10 <= timestamp:
                self.logger[message] = timestamp
                return True
            
            return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
