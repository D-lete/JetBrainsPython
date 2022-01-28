profits = []
profit_forecast = []

for cost, revenue in zip(costs, revenues):
    profits.append(revenue - cost)
for month, profit in zip(months, profits):
    print(month, profit)
