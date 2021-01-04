#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the tip calculator.")

bill_amount = (float(input("What is your bill amount? $")))
 
percentage = (int(input("What percent of the tip you would like to pay, 10, 12 or 15?: ")))

split = (int(input("How many of you are splitting the bill? ")))

pay = (bill_amount / split ) 

tip_pay = pay * (percentage / 100) 

each_pay = round(pay + tip_pay, 2)

print(f"Each should pay: ${each_pay}.")