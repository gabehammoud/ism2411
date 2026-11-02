# reflection 1

# The most surprising thing about Python lists is how easily they can be
# modified, sorted, and sliced without having to create a new list each time.
# I also found it interesting that negative indexing allows you to access
# items starting from the end of a list.

# reflection 2

# At my restaurant job, Python lists could have helped organize and track
# daily sales totals. Instead of manually calculating totals and averages
# in Excel, I could use Python to automatically process the sales data
# and identify the highest and lowest sales days.


# exercise 1

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print("Exercise 1:")
print(inventory)
print(len(inventory))

# exercise 2 

print("\nExercise 2:")
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# exercise 3

print("\nExercise 3:")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# exercise 4

print("\nExercise 4:")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# exercise 5 

print("\nExercise 5:")
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError:
    print("TypeError caught: Tuples cannot be changed.")
    print("Tuples are useful for coordinates because they keep values fixed.")
print(coords)

# exercise 6 

print("\nExercise 6:")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
best = max(sales)
worst = min(sales)
print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", best)
print("Worst:", worst)

# exercise 7 

print("\nExercise 7:")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)
print("Original prices:", prices)
print("Discounted prices:", discounted)

# exercise 8 

print("\nExercise 8:")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)
high_sales_average = sum(high_sales) / len(high_sales)
print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", round(high_sales_average, 2))