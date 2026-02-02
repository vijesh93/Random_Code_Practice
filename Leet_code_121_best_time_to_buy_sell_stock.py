class Solution:

    def __init__(self):
        
        self.buy_day: int = 0
        self.sell_day: int = 0

        self.buy_price: int = 0
        self.sell_price: int = 0

        self.profit: int = 0
        
        self.prices = [0]
        self.verbose = False
    
    def buy(self, day_index: int):
        self.buy_day = day_index
        self.buy_price = self.prices[day_index]
        if self.verbose:
            print('********************************Day and price Bought: ', day_index, '    $ ', self.buy_price)
        self.update_profit()
        
    def sell(self, day_index: int):
        self.sell_day = day_index
        self.sell_price = self.prices[day_index]
        if self.verbose:
            print('********************************Day and price Sell: ', day_index, '    $ ', self.sell_price)
        self.update_profit()
         
    def update_profit(self):
        self.profit = self.prices[self.sell_day] - self.prices[self.buy_day]
        if self.verbose:
            print('********************************Profit: ', self.profit)

    def maxProfit(self, prices: List[int], verbose: bool = False) -> int:
        
        self.verbose = verbose
        self.prices = prices
        # profit_track_dict = {}
        self.buy(0)
        self.sell(0)
        theoritical_buy_day = 0
        theoritical_buy_price = prices[theoritical_buy_day]
        # max_price_day = 0

         # Compute max profit
        for day_index, day_price in enumerate(prices):
            if day_index == 0:
                continue
            if verbose:
                print("########################")
                print("Day: ", day_index, "  Price: ", day_price)
                print("self.buy_day: ", self.buy_day)
                print("self.buy_price: ", self.buy_price)
                print("*****")
                print("self.sell_day: ", self.sell_day)
                print("self.sell_pricd: ", self.sell_price)
                print("*****")
                print("theoritical_buy_day: ", theoritical_buy_day)
                print("theoritical_buy_price: ", theoritical_buy_price)
            # Phase 1
            if day_price > self.sell_price:
                self.sell(day_index=day_index)
                if self.verbose:
                    print('Skipping')
                continue

            # Phase 2
            if day_price < self.buy_price:
                 
                theoritical_buy_day = day_index
                theoritical_buy_price = day_price
                if self.verbose:
                    print("Updated theoritical_buy_day: ", theoritical_buy_day)
                    print("Updated theoritical_buy_price: ", theoritical_buy_price)

            # Phase 3
            if day_price - theoritical_buy_price > self.profit:
                self.buy(day_index=theoritical_buy_day)
                self.sell(day_index=day_index)

        return max(self.profit, 0)
        

if __name__ == "__main__":
        print(Solution().maxProfit(prices=[7,1,5,3,6,4], verbose=True))
