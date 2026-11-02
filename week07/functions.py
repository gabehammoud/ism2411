#1 The first bug I noticed was a missing colon on line 10.
#  I found it by looking at the traceback after running the script. 
# This shows that I ran the program first to identify any errors, 
# which is my preferred way of debugging.
#2 The function first checks which tier applies. After determining the tier,
#  it calculates the discount based on the price and returns the final price.
#  I am not entirely sure what the question is asking, but the function can be 
# used without needing to read the code. Even if someone does look at the code, 
# it is written in a way that is easy to understand.
#3 I did not use AI to complete the assignment outside of the part where it was 
# specifically required. I mainly followed the teacher's instructions. The AI portion 
# did not really improve my understanding of the material because I found that I learned
#  more by working through the problems myself.

# exercise 1

def calculate_tax(price, rate):
    return price*rate
tax1=calculate_tax(100, .07)
tax2=calculate_tax(250, .08)
print(f"Tax for $100 at 7%: ${tax1:,.2f}")
print(f"Tax for $250 at 8%: ${tax2:,.2f}")
print(f"Another tax: ${calculate_tax(150, 0.05):,.2f}")

# exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price*.85
    elif tier == "silver":
        return price*.9
    elif tier == "bronze":
        return price*.95
    else:
        return price
price = 200
tiers = ["gold","silver","bronze","none"]
for tier in tiers:
    print(f"Tier: {tier}: Price: ${apply_discount(price, tier)}")

# exercise 3

discounted=apply_discount(200, "gold")
tax=calculate_tax(discounted, 0.07)
after_tax=discounted+tax
print(f"After gold discount: ${discounted:,.2f}")
print(f"After tax: ${after_tax:,.2f}")
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax
print(f"Final price: ${final_price(200, 'gold', .07):,.2f}")

# exercise 4

orders = [(200, "gold"),(150,"silver"),(80, "bronze"),(500,"none")]
for price, tier in orders:
    total = final_price(price, tier, .07)
    print(f"Price: ${price:,.2f}, Tier: {tier}, Final: ${total:,.2f}")

# exercise 6

x = 100 #global
def double_it():
    x = 999   # local 
    return x * 2
print(x)           
print(double_it()) 
print(x)           
#100.
#999 
#100