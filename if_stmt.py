# if statements

amount = float(input("Enter the amount of product : "))

if amount >= 1000:
    discount = amount * 10/100
    print(f"Discount amount is : {discount}")
    final_amount = amount - discount
    print(f"Final amount is : {final_amount}")
elif amount >= 15000:
    discount = amount * 15/100
    print(f"Discount amount is : {discount}")
    final_amount = amount - discount
    print(f"Final amount is : {final_amount}")
else:
    print("Sorry!, You are not eligible for discount")
