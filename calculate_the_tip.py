# Your goal is to find out exactly how much tip you should give after receiving a service.
# In this scenario, ask for the total bill. Then display the tip for 18%, 20% and 25%.
import math
bill = float(input("What's the total bill for today, please???"))

tip_18 = bill*(18/100)
total_bill1 = math.ceil(bill + tip_18)

tip_20 = bill*(20/100)
total_bill2 = math.ceil(bill + tip_20)

tip_25 = bill*(25/100)
total_bill3 = math.ceil(bill + tip_25)
print(f'18% tip is {tip_18}, which brings your total to {total_bill1}.')
print(f'20% tip is {tip_20}, which brings your total to {total_bill2}.')
print(f'18% tip is {tip_25}, which brings your total to {total_bill3}.')