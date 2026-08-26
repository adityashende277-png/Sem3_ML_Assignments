prices = " 120, 45 , 300 ,80, 95 "

price_list = []

for price in prices.split(","):
    price_list.append(int(price.strip()))

total = sum(price_list)
highest = max(price_list)
average = total / len(price_list)

print(f"Total   : {total}")
print(f"Highest : {highest}")
print(f"Average : {average:.2f}")