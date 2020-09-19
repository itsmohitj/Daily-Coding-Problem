"""
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

"""

def maxProfit(prices):
        sell_val = 0
        purchase_val = float('inf')
        profit = 0
        for i in prices:
            if i < purchase_val:
                purchase_val = i
            sell_val = i
            if sell_val - purchase_val > profit:
                profit = sell_val-purchase_val
        return profit

# Time Complexity = O(n)
# Space Complexity = O(1)
