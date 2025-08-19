# Practice Initialization of Python Code Demo 


# this is Demo - Sales Tax Calculator 


try:
    amount = float(input("Enter the amount of Product : \n"))
    tax_rate = float(input("Enter the sales tax rate (in percentage): \n"))
    total = amount + (amount * tax_rate / 100)
    print(f"The total amount after adding sales tax is: {total:.2f}") # This code calculates the total amount after applying sales tax to a given product amount.

except ValueError:
    print("Please Enter a valid number for amount and tax rate.") # This code handles the case where the user inputs an invalid number, prompting them to enter a valid number.

