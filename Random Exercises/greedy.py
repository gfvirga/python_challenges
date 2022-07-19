def bestDaysToBuyAndSell(arr):
  # Write your code here
  
  return [arr.index(min(arr)),arr.index(max(arr))]

print(bestDaysToBuyAndSell([100, 180, 260, 310, 40, 535, 695]))