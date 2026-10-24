class Solution(object):
    def maxProfit(self, prices):
      priceBuy = float('inf')
      priceSell = 0

      for i in prices:
        priceBuy = min(priceBuy, i)
        priceSell = max(priceSell, i - priceBuy)
        
      return priceSell
