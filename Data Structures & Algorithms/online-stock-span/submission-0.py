class StockSpanner:

    def __init__(self):
        self.stock = []
        self.length = 0

    def next(self, price: int) -> int:
        if self.length == 0:
            self.stock.append(price)
            self.length += 1
            return 1

        days = 1
        r = self.length - 1
        while r >= 0 and price >= self.stock[r]:
            days += 1
            r -= 1
                 
        self.stock.append(price)
        self.length += 1
        return days

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)