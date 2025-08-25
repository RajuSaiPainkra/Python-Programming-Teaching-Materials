# match case statments Check

"""
def weekday(day):
    match day:
        case 0 : return "Sunday"
        case 1 : return "Monday"
        case 2 : return "Tuesday"
        case 3 : return "Wednesday"
        case 4 : return "Thursday"
        case 5 : return "Friday"
        case 6 : return "Saturday"
        case _ : return "Enter Valid Day Number" 

print(weekday(1))
"""

# rewrite the code the check subject Examination



day = str(input("Enter the Day in the Weeks : \n "))
def days(day):
    match day:
        case "Monday" : return "English Philosophy"
        case "Tuesday" : return "Mathematics"
        case "Wednesday" : return "Science"
        case "Thursday" : return "Social Studies"
        case "Friday" : return "Computer Science and Infomation Technology"
        case "Saturday" : return "Economics and Monetry Studies"
        case "Sunday" : return "Holiday"
        case _ : return "Enter Valid Day Name "

print("Your Examination subject is : ", days(day), "Make sure ready for Examination.")