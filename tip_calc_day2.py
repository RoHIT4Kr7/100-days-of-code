print("Welcome to the tip calculator. ")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10,12, or 15?"))
total_bill= bill + (tip%bill)
# print(f"bill is {total_bill}")
split = int(input("How many people to split the bill? "))
perheadbill=total_bill/split
print(f"Each person should pay :${perheadbill}")
