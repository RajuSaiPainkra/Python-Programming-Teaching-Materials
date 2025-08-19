# Practice Initialization of Python Code Demo 


# this is Demo - Sales Tax Calculator 



amount = float(input("Enter the amount of Product : \n"))
tax_rate = float(input("Enter the sales tax rate (in percentage): \n"))
total = amount + (amount * tax_rate / 100)
print(f"The total amount after adding sales tax is: {total:.2f}") # This code calculates the total amount after applying sales tax to a given product amount.