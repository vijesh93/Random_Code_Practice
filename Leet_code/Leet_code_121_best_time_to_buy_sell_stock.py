from typing import List


class Solution:

    def __init__(self):
        
        self.buy_day: int = 0
        self.sell_day: int = 0

        self.buy_price: int = 0
        self.sell_price: int = 0

        self.theoritical_buy_day: int = 0
        self.theoritical_buy_price: int = 0

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

        # While selling, update the last best buy price
        if self.buy_price > self.theoritical_buy_price:
            self.buy(day_index=self.theoritical_buy_day)
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
        self.theoritical_buy_day = 0
        self.theoritical_buy_price = prices[self.theoritical_buy_day]
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
                print("self.sell_price: ", self.sell_price)
                print("*****")
                print("theoritical_buy_day: ", self.theoritical_buy_day)
                print("theoritical_buy_price: ", self.theoritical_buy_price)
        
            # If price is increased since the last sell price
            if day_price > self.sell_price:
                self.sell(day_index=day_index)

            # If the price is reduced compared the buy day
            if day_price < self.buy_price and day_price < self.theoritical_buy_price:
                self.theoritical_buy_day = day_index
                self.theoritical_buy_price = day_price
            
            if (day_price - self.theoritical_buy_price) > self.profit:
                self.sell(day_index=day_index)        
        
        return max(self.profit, 0)


class Solution_GPT:
    # Way better and efficient ;p
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy_price = prices[0] # This is your "theoretical_buy_price"
        
        for price in prices:
            # 1. Update our "theoretical" best buy price if we find a new low
            if price < min_buy_price:
                min_buy_price = price
            
            # 2. See if selling at the current price beats our best record
            current_profit = price - min_buy_price
            if current_profit > max_profit:
                max_profit = current_profit
                
        return max_profit
    

if __name__ == "__main__":
        print(Solution().maxProfit(prices=[2,1,2,1,0,1,2], verbose=True))
