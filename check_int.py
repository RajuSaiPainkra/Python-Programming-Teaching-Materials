# Write a program to check if a number is positive, negative, or zero.
try:
    num = int(input("Enter the Integer Value : \n"))

    if num > 0:
        print(f"Input Value : {num}\nInput Value is Positive Value")
    elif num < 0:
        print(f"Input Value : {num}\nInput Value is Negative Value")
    elif num == 0:
        print(f"Input Value : {num}\nInput Value is Zero Value")
    else:
        print(f"Input Value : {num}\nInput Value is Invalid") # this is optional, 

except ValueError:
    print("Please!, Enter the Integer Value.")